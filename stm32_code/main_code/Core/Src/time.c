#include "stm32l4xx.h"

void delayMicroseconds(int delay){
	int startingValue = TIM5->CNT;
	int readValue = startingValue;
	while(readValue-startingValue<delay){
		readValue =TIM5->CNT;
	}
}
