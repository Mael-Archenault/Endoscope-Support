#include "stm32l4xx.h"
#include "time.h"
#include "drivers.h"
#include <math.h>


int step_time_us = 500000; // minimum 1us

int t_pulse_length = 1; //length moved with 1 pulse (in mm)
int r_pulse_angle = 1; //angle turned with 1 pulse (in °)

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
	sendNPulse(1, T_MOTOR);
	delayMicroseconds(1000000);
	sendNPulse(dx, T_MOTOR);
	

	// int nb_pulses = (int)((float)dx/(float)t_pulse_length);
	// sendNPulse(nb_pulses, T_MOTOR);
}

void rotate(int dtheta){
	sendNPulse(2, T_MOTOR);
	delayMicroseconds(1000000);
	sendNPulse(dtheta, T_MOTOR);
	// int nb_pulses = (int)((float)dtheta/(float)r_pulse_angle);
	// sendNPulse(nb_pulses, R_MOTOR);
}


void setMicrosteppingMode(int stepping_mode){

	// Parameter n define the stepping mode
	// The step is 1/n
	// with n in {1,2,4,8,16}

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
}

void setSleep(int n_driver, int state){
	if (n_driver==R_MOTOR){
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_10, state);
    }

    else if (n_driver==T_MOTOR){
        HAL_GPIO_WritePin(GPIOB, GPIO_PIN_3, state);
    }
}

