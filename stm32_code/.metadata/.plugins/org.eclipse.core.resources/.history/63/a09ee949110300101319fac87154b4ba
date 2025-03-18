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

        
        if (state==LISTENING_STATE){

            if (strcmp(argv[0],"move")==0){
                state = MOVING_STATE;
            }

            else if (strcmp(argv[0],"turn")==0){
                state = TURNING_STATE;
            }

            else if (strcmp(argv[0],"change")==0){
                state = VARIABLE_CHANGE_STATE;
            }

            else if (strcmp(argv[0],"home")==0){
                state = HOMING_STATE;
            }
            else if (strcmp(argv[0],"picture")==0){
                state = PICTURING_STATE;
            }

            else if (strcmp(argv[0],"getFirmware")==0){
                state = FIRMWARE_SENDING_STATE;
            }

            else if (strcmp(argv[0],"moveTo")==0){
                state = MOVING_TO_STATE;
            }
            
            else if (strcmp(argv[0],"computeStep")==0){
                state = STEP_COMPUTING_STATE;
            }
            else if (strcmp(argv[0],"play")==0){
                state = CAPTURING_STATE;
                
            }
            else if (strcmp(argv[0], "playTestSequence")== 0){
                state = TESTING_SEQUENCE_STATE; 
            }

    
        }

        if (state == CAPTURING_STATE){
            if (strcmp(argv[0],"stop")==0){
                state = STOPPING_STATE;
            }
            if (strcmp(argv[0],"pause")==0){
                // Notifying pc of the change of steps
                char message[BUFF_SIZE] = {" "};
                snprintf(message, sizeof(message), "logCapture Paused capture");
                transmit_to_pc(&message);
                state = PAUSED_STATE;
            }
    
        }
        if (state == TESTING_SEQUENCE_STATE){
            if (strcmp(argv[0],"stopTestSequence")==0){
                state = STOPPING_SEQUENCE_STATE;
            }
            if (strcmp(argv[0],"pauseTestSequence")==0){
                // Notifying pc of the change of steps
                char message[BUFF_SIZE] = {" "};
                snprintf(message, sizeof(message), "logTest Paused the test of the capture sequence");
                transmit_to_pc(&message);
                state = PAUSED_STATE;
            }
    
        }
        if (state == PAUSED_STATE){
            if (strcmp(argv[0],"play")==0){
                state = CAPTURING_STATE;
            }
            if (strcmp(argv[0],"stop")==0){
                state = STOPPING_STATE;
            }

            if (strcmp(argv[0],"playTestSequence")==0){
                state = TESTING_SEQUENCE_STATE;
            }
            if (strcmp(argv[0],"stopTestSequence")==0){
                state = STOPPING_SEQUENCE_STATE;
            }
        }
        


        HAL_UART_Receive_IT(&huart2, &command, BUFF_SIZE);  // Restart reception

    }
}

void transmit_to_pc(char** message){
    HAL_UART_Transmit(&huart2, message, BUFF_SIZE, 1000);
}
