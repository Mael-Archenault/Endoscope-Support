#include "stm32l4xx.h"
#include "communication.h"
#include "main.h"
#include "init.h"


 
extern TIM_HandleTypeDef htim5;
extern TIM_HandleTypeDef htim16;


extern UART_HandleTypeDef huart2;

extern command[BUFF_SIZE];

VAR variables[NB_VAR]= {
        {"translation_starting_point", 0, "mm"},
        {"translation_ending_point", 0, "mm"},
        {"translation_number_of_points",0, ""},
        {"translation_speed",0, "%"},
        {"rotation_starting_point", 0, "°"},
        {"rotation_ending_point", 0, "°"},
        {"rotation_number_of_points",0, ""},
        {"rotation_speed",0,"%"},
        {"exposure_time",0, "s"},
        {"saving_time",0, "s"},
        {"margin_time",0,"s"}
    };

int find_value(char* name){
    for (int i = 0; i < NB_VAR; i++){
        if (strcmp(name, variables[i].name) == 0){
            return variables[i].value;
        }
    }
}


void init(){
    // Initializing the time reference counter
    __HAL_TIM_SET_COUNTER(&htim5, 0);  // Reset the counter to 0
    HAL_TIM_Base_Start(&htim5);
   
    // Initializing the IR emmition timer
    HAL_TIM_Base_Start(&htim16);
    TIM16->CCR1 = 1000; // setting the compare register to half the period (to generate a square signal)
    HAL_TIM_PWM_Start(&htim16, TIM_CHANNEL_1);
   
   
    // Initializing the command buffer and receiving command over UART
    HAL_UART_Receive_IT(&huart2, command, BUFF_SIZE);
   
    // Initializing all Capture Variables


}
