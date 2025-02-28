#include <stdio.h>
#include <stdlib.h>


#include "drivers.h"
#include "communication.h"
#include "ir_led.h"

#include "main.h"
#include "mainloop.h"

#include "time.h"
#include "states.h"

extern UART_HandleTypeDef huart2;

extern VAR variables[NB_VAR];

char command[BUFF_SIZE];

int argc = 0;
char* argv[10];

char firmware[5] = "1.0.0";


int state = 0;

// Capturing temporary variables

extern int current_x;
extern int current_theta;

float t_step = 100;
float r_step = 100;

int total_picture_number = 0;
int total_time_seconds = 0;

int pictures_taken = 0;
int pictures_taken_for_this_angle = 0;
int angles_explored = 0;

int translation_index = 0;
int rotation_index = 0;


void run(){
    while (1){
        if (state == MOVING_STATE){
            int distance = atoi(argv[1]);
            move(distance, 0, 0);
            // Notifying pc of the successful translation
            // char message[BUFF_SIZE] = {" "};
            // snprintf(message, sizeof(message), "logTest Translated of %d mm", distance);
            // transmit_to_pc(&message);

            state = LISTENING_STATE;
            
        }
      
        if (state == TURNING_STATE){
            int angle = atoi(argv[1]);
            move(0, angle, 0);

            state = LISTENING_STATE;
        }

        if (state == VARIABLE_CHANGE_STATE){
            char unit[64];
            for (int i = 0; i < NB_VAR; i++){
                if (strcmp(argv[1], variables[i].name) == 0){
                    variables[i].value = atoi(argv[2]);
                    strncpy(unit, variables[i].unit, sizeof(unit));
                    break;
                }
            }

            // Notifying pc of the successful variable change
            char message[BUFF_SIZE] = {" "};
            snprintf(message, sizeof(message), "logSettings Variable : %s set to : %d %s", argv[1], atoi(argv[2]), unit);
            transmit_to_pc(&message);

            state = LISTENING_STATE;
        }

        if (state == CAPTURING_STATE){

            char message[BUFF_SIZE] = {" "};
            snprintf(message, sizeof(message), "progress %d %d %d", pictures_taken, pictures_taken_for_this_angle, angles_explored);
            transmit_to_pc(&message);
            memset(message, 0, BUFF_SIZE);

            int x = find_value("translation_starting_point") + (int)(translation_index*t_step);
            int theta = find_value("rotation_starting_point")+ (int)(rotation_index*t_step);
            move_to(x, theta,1);
            translation_index ++;

            
            takePicture(1);
            pictures_taken++;
            pictures_taken_for_this_angle++;

            // Notifying pc of the progress of the capture
           
            snprintf(message, sizeof(message), "progress %d %d %d", pictures_taken, pictures_taken_for_this_angle, angles_explored);
            transmit_to_pc(&message);
            memset(message, 0, BUFF_SIZE);

            int total_time = find_value("exposure_time")+find_value("saving_time")+find_value("margin_time");
            delayMicroseconds(total_time*1000000);

            if (current_x >= find_value("translation_ending_point")){
                if (current_theta >= find_value("rotation_ending_point")){
                    snprintf(message, sizeof(message), "logCapture End of the Capture");
                    transmit_to_pc(&message);
                    memset(message, 0, BUFF_SIZE);
                    
                    snprintf(message, sizeof(message), "logCapture Return to the home position");
                    transmit_to_pc(&message);
                    memset(message, 0, BUFF_SIZE);
                    
                    angles_explored ++;
                    snprintf(message, sizeof(message), "progress %d %d %d", pictures_taken, pictures_taken_for_this_angle, angles_explored);
                    transmit_to_pc(&message);
                    memset(message, 0, BUFF_SIZE);

                    move_to(0,0,1);
                    angles_explored = 0;
                    pictures_taken = 0;
                    pictures_taken_for_this_angle = 0;

                    translation_index = 0;
                    rotation_index = 0;

                    snprintf(message, sizeof(message), "end capture");
                    transmit_to_pc(&message);
                    memset(message, 0, BUFF_SIZE);
                    
                    
                    state = LISTENING_STATE;
                }
                else {
                    translation_index = 0;
                    rotation_index++;

                    angles_explored++;
                    pictures_taken_for_this_angle = 0;
                }
            }  

        }

        if (state == TESTING_SEQUENCE_STATE){

            int x = find_value("translation_starting_point") + (int)(translation_index*t_step);
            int theta = find_value("rotation_starting_point")+ (int)(rotation_index*t_step);
            move_to(x, theta,0);
            translation_index ++;
            
            int total_time = 1;
            delayMicroseconds(total_time*1000000);

            if (current_x >= find_value("translation_ending_point")){
                if (current_theta >= find_value("rotation_ending_point")){
                    
                    char message[BUFF_SIZE] = {0};
                    snprintf(message, sizeof(message), "logTest End of the Sequence Test");
                    transmit_to_pc(&message);
                    memset(message, 0, BUFF_SIZE);
                    
                    snprintf(message, sizeof(message), "logTest Return to the home position");
                    transmit_to_pc(&message);
                    memset(message, 0, BUFF_SIZE);
                    
                    move_to(0,0,0);

                    

                    translation_index = 0;
                    rotation_index = 0;

                    snprintf(message, sizeof(message), "end testSequence");
                    transmit_to_pc(&message);
                    memset(message, 0, BUFF_SIZE);
                    
                    state = LISTENING_STATE;
                }
                else {
                    translation_index = 0;
                    rotation_index++;

                }
            }


        }

        if (state == HOMING_STATE){
            home_motors();

            // Notifying pc of the successful homing
            char message[BUFF_SIZE] = {" "};
            snprintf(message, sizeof(message), "logTest Homed motors | Position (0 mm, 0°)");
            transmit_to_pc(&message);

            state = LISTENING_STATE;
        }

        if (state == STOPPING_STATE){
            // Notifying pc of the successful homing
            char message[BUFF_SIZE] = {" "};
            snprintf(message, sizeof(message), "logCapture Stopped capture | return to home position");
            transmit_to_pc(&message);
            memset(message, 0, BUFF_SIZE);

            

            move_to(0,0,1);

            snprintf(message, sizeof(message), "end capture");
            transmit_to_pc(&message);
            memset(message, 0, BUFF_SIZE);

            angles_explored = 0;
            pictures_taken = 0;
            pictures_taken_for_this_angle = 0;

            translation_index = 0;
            rotation_index = 0;

            state = LISTENING_STATE;
        }

        if (state == STOPPING_SEQUENCE_STATE){
            // Notifying pc of the successful homing
            char message[BUFF_SIZE] = {" "};
            snprintf(message, sizeof(message), "logTest Stopped the test of the capture sequence | return to home position");
            transmit_to_pc(&message);
            memset(message, 0, BUFF_SIZE);

            


            move_to(0,0,0);

            snprintf(message, sizeof(message), "end testSequence");
            transmit_to_pc(&message);
            memset(message, 0, BUFF_SIZE);

            translation_index = 0;
            rotation_index = 0;

            state = LISTENING_STATE;
        }

        if (state == PICTURING_STATE) {
            takePicture(0);
            state = LISTENING_STATE;
        }

        if (state == FIRMWARE_SENDING_STATE) {

            // Notifying pc of the firmware version
            char message[BUFF_SIZE] = {" "};
            snprintf(message, sizeof(message), "firmware %s", firmware);
            transmit_to_pc(&message);
            state = LISTENING_STATE;
        }

        if (state == MOVING_TO_STATE) {

            move_to(atoi(argv[1]), atoi(argv[2]), 0);

            state = LISTENING_STATE;
        }

        if (state == STEP_COMPUTING_STATE){

            t_step = (float)(find_value("translation_ending_point")-find_value("translation_starting_point"))/(float)(find_value("translation_number_of_points")-1);
            r_step = (float)(find_value("rotation_ending_point")-find_value("rotation_starting_point"))/(float)(find_value("rotation_number_of_points")-1);

            total_picture_number = find_value("translation_number_of_points")*find_value("rotation_number_of_points");
            update_speeds(find_value("translation_speed"), find_value("rotation_speed"));

            /////////////////// Evaluating the capture time //////////////////////////////////
            total_time_seconds = 0;
            // time of translations
            total_time_seconds += 2*get_translation_time((int)t_step)*(find_value("translation_number_of_points")-1)*find_value("rotation_number_of_points");
            
            // time of rotations
            total_time_seconds += 2*get_rotation_time((int)r_step)*(find_value("rotation_number_of_points")-1);
            
            // time of waiting
            total_time_seconds += (find_value("exposure_time")+find_value("saving_time")+find_value("margin_time"))*total_picture_number;

            // Notifying pc of the change of steps

            char message[BUFF_SIZE] = {" "};
            snprintf(message, sizeof(message), "estimatedTime %d",total_time_seconds);
            transmit_to_pc(&message);
            memset(message, 0, sizeof(message));

            
            snprintf(message, sizeof(message), "logSettings Changed steps | Translation step : %f mm, Rotation step : %f°", t_step, r_step);
            transmit_to_pc(&message);
            memset(message, 0, sizeof(message));

            snprintf(message, sizeof(message), "total %d %d %d %d %d",find_value("translation_ending_point"),find_value("rotation_ending_point"), find_value("translation_number_of_points"), find_value("rotation_number_of_points"), total_picture_number);
            transmit_to_pc(&message);

            state = LISTENING_STATE;
        }

    }
}

