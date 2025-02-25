#include "stm32l4xx.h"

void delayMicroseconds(int delay){
	int startingValue = TIM5->CNT;

	// Handling the timer overflow
	if (startingValue >= 4294967295-delay-1){
		TIM5->CNT = 0;
		startingValue = 0;
	}

	int readValue = startingValue;
	while(readValue-startingValue<delay){
		readValue =TIM5->CNT;
	}
}
