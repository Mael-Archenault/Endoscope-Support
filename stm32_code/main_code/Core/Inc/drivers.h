void send1Pulse(int n_driver);
void sendNPulse(int N, int n_driver);
void translate();
void rotate();

void setDirection(int n_driver, int direction);
void setEnable(int n_driver, int state);
void setReset(int n_driver, int state);
void setSleep(int n_driver, int state);

void setMicrosteppingMode(int n);




#define FULL_STEP 0;
#define HALF_STEP 1;
#define QUARTER_STEP 2;
#define EIGHTH_STEP 3;
#define SIXTEENTH_STEP 4;


#define R_MOTOR 1
#define T_MOTOR 2

#define BACKWARD 0
#define FORWARD 1

#define ENABLE 0
#define DISABLE 1


