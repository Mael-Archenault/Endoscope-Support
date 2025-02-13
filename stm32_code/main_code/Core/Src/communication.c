#include "communication.h"
#include "stm32l4xx.h"
#include "drivers.h"
#include "states.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>



extern UART_HandleTypeDef huart2;


extern char command[BUFF_SIZE];

int handled = 0;

extern int state;

extern int argc;
extern char* argv[10];



void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) {
    if (huart->Instance == USART2) {  // Check which UART triggered the callback
        // Process received data
    	
        
        if (state==LISTENING_STATE){
            char* token;
            argc = 0;
            const char delim[] = " ";

            // Storing the command name
            token = strtok(command, delim);
            argv[argc] = token;
            argc++;
            
            // Storing the command parameters
            while(token!=NULL){
                token = strtok(NULL, delim);
                argv[argc] = token;
                argc++;
            }


            if (strcmp(argv[0],"move")==0){
                state = MOVING_STATE;
            }

            else if (strcmp(argv[0],"turn")==0){
                state = TURNING_STATE;
            }
        }


        HAL_UART_Receive_IT(&huart2, command, BUFF_SIZE);






        HAL_UART_Receive_IT(&huart2, &command, BUFF_SIZE);  // Restart reception
    }
}
