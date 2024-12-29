#include <stdio.h>
#include "stm32l4xx.h"
#include <stm32l4xx_hal.h>



int readPin(){
	int res = HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_5);
	return res;
}


int detectSeq(){
	printf("\n\rStarting wait...\n\r");
	int state = 1;

	while (state==1){
		state = readPin();
	}

	printf("End of wait\n\r");

	for (int i = 0; i<15; i++){
		HAL_Delay(1);
		state = readPin();
		printf("State after 9ms = %d\n\r", state);
	}
	if (state==1){
		return 1;
	}
	return 0;

}



