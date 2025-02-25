#include "stm32l4xx.h"
#include "time.h"
#include "drivers.h"
#include <math.h>


int step_time_us = 500000; // minimum 1us

int t_pulse_length = 1; //length moved with 1 pulse (in mm)
int r_pulse_angle = 1; //angle turned with 1 pulse (in °)


int current_x = 0;
int current_theta = 0;

void send1Pulse(int n_driver){

	uint16_t GPIO_PIN;
	GPIO_PIN = (n_driver==T_MOTOR)?GPIO_PIN_5:GPIO_PIN_7;
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN, 1);
	delayMicroseconds(step_time_us);
	HAL_GPIO_WritePin(GPIOA, GPIO_PIN, 0);
	delayMicroseconds(step_time_us);

}

void sendNPulse(int N, int n_driver){
	for (int i = 0; i<N; i++){
		send1Pulse(n_driver);
	}
}


void translate(int dx){

	int coeff;
	if (dx >= 0){
        coeff = 1;
    } else {
        coeff = -1;
		setDirection(T_MOTOR, BACKWARD);
    }
	
	int nb_pulses = (int)((float)(coeff*dx)/(float)t_pulse_length);
	sendNPulse(nb_pulses, T_MOTOR);
	
	if (dx < 0){
		setDirection(T_MOTOR, FORWARD);
	}

	
}

void move_to(int x, int theta){
	int dx = x - current_x;
    int dtheta = theta - current_theta;

    translate(dx);
    rotate(dtheta);

	current_x = x;
	current_theta = theta;

}

void rotate(int dtheta){
	int coeff;
	if (dtheta >= 0){
        coeff = 1;
    } else {
		coeff = -1;
		setDirection(R_MOTOR, BACKWARD);
    }
	
	int nb_pulses = (int)((float)(coeff*dtheta)/(float)t_pulse_length);
	sendNPulse(nb_pulses, R_MOTOR);
	
	if (dtheta < 0){
		setDirection(R_MOTOR, FORWARD);
	}
}


void setMicrosteppingMode(int stepping_mode){

	// Possible Parameters:
	//  -FULL_STEP
	//  -HALF_STEP
	//  -QUARTER_STEP
	//  -EIGHT_STEP
	//  -SIXTEENTH_STEP

	/*
	   Microstepping Resolution Truth Table

	   | MS1 | MS2 | MS3 | Microstep Resolution | Excitation Mode  |
	   |-----|-----|-----|----------------------|------------------|
	   |  L  |  L  |  L  | Full Step            | 2 Phase          |
	   |  H  |  L  |  L  | Half Step            | 1-2 Phase        |
	   |  L  |  H  |  L  | Quarter Step         | W1-2 Phase       |
	   |  H  |  H  |  L  | Eighth Step          | 2W1-2 Phase      |
	   |  H  |  H  |  H  | Sixteenth Step       | 4W1-2 Phase      |

	   Note: by setting the stepping mode in {0,1,2,3,4}, MSx is just the x-th bits of the stepping mode
	*/
	int MS1 = stepping_mode&0x1;
	int MS2 = (stepping_mode&0x2)>>1;
	int MS3 = (stepping_mode&0x4)>>2;


	// PA9 -> MS1
	// PC7 -> MS2
	// PB6 -> MS3

	HAL_GPIO_WritePin(GPIOA, GPIO_PIN_9, MS1);
	HAL_GPIO_WritePin(GPIOC, GPIO_PIN_7, MS2);
	HAL_GPIO_WritePin(GPIOB, GPIO_PIN_6, MS3);


}

void setDirection(int n_driver, int direction){

	if (n_driver==T_MOTOR){
		HAL_GPIO_WritePin(GPIOA, GPIO_PIN_8, direction);
	}

	else if (n_driver==R_MOTOR){
		HAL_GPIO_WritePin(GPIOB, GPIO_PIN_10, direction);
	}

	// Required time to wait before sending a step : 200 ns
	delayMicroseconds(1);
}

void setEnable(int n_driver, int state){
	if (n_driver==R_MOTOR){
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_0, state);
    }

    else if (n_driver==T_MOTOR){
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_1, state);
    }
}

void setReset(int n_driver, int state){
	if (n_driver==R_MOTOR){
        HAL_GPIO_WritePin(GPIOB, GPIO_PIN_5, state);
    }

    else if (n_driver==T_MOTOR){
        HAL_GPIO_WritePin(GPIOB, GPIO_PIN_4, state);
    }

	// Required time to wait before sending a step : 200 ns
	delayMicroseconds(1);
}

void setSleep(int n_driver, int state){
	if (n_driver==R_MOTOR){
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_10, state);
    }

    else if (n_driver==T_MOTOR){
        HAL_GPIO_WritePin(GPIOB, GPIO_PIN_3, state);
    }
	
	// Required time to wait before sending a step : 1 ms
	delayMicroseconds(2000);
}


void initializeDrivers(){
	setMicrosteppingMode(HALF_STEP);

	setReset(T_MOTOR, DISABLE);
	setReset(R_MOTOR, DISABLE);

	setSleep(T_MOTOR, DISABLE);
	setSleep(R_MOTOR, DISABLE);

	setDirection(T_MOTOR, FORWARD);
	setDirection(R_MOTOR, FORWARD);

	setEnable(T_MOTOR, ENABLE);
	setEnable(R_MOTOR, ENABLE);

}

void home_motors(){
	setDirection(T_MOTOR, BACKWARD);

	int flag = 0;


    while(HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_4) == 0){
		send1Pulse(T_MOTOR);
	}

	current_x = 0;
	current_theta = 0;
}

