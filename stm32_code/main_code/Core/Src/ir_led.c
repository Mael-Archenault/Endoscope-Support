#include "stm32l4xx.h"

extern TIM_HandleTypeDef htim16;

// IR CODE //
void sendBit1() {
    // Start PWM for 1200 µs for logic "1" pulse
    HAL_TIM_PWM_Start(&htim16, TIM_CHANNEL_1);
    delayMicroseconds(1200);

    // Stop PWM to represent "off" period of 600 µs
    HAL_TIM_PWM_Stop(&htim16, TIM_CHANNEL_1);
    delayMicroseconds(600);
}

void sendBit0() {
    // Start PWM for 600 µs for logic "0" pulse
    HAL_TIM_PWM_Start(&htim16, TIM_CHANNEL_1);
    delayMicroseconds(600);  // Custom microsecond delay function

    // Stop PWM to represent "off" period of 600 µs
    HAL_TIM_PWM_Stop(&htim16, TIM_CHANNEL_1);
    delayMicroseconds(600);  // Same low duration as the pulse for "0"
}

void sendSIRCSData(int data) {

	// Start pulse
    HAL_TIM_PWM_Start(&htim16, TIM_CHANNEL_1);
    delayMicroseconds(2400);  // 2.4 ms "on" for start pulse
    HAL_TIM_PWM_Stop(&htim16, TIM_CHANNEL_1);
    delayMicroseconds(600);  // 0.6 ms "off" period

    // Transmit 32 bits of data
    for (int i = 0; i < 20; i++) {

        if (data & (1UL << (19 - i))) {

            sendBit1();

        } else {

            sendBit0();

        }
    }

}

void takePicture(){
	int data = 0b10110100101110001111;
	for (int i = 0; i<3; i++){
	  sendSIRCSData(data);
	}
}
