// firmware.c
//Waits for strings like "SET_SPEED 100" or "STOP".
//Parses and executes them directly on hardware.
//Responds back with text over UART.

#include <stdio.h>
#include <string.h>
#include "uart.h"
#include "motor.h"

void processCommand(const char *cmd){
  if (strncmp(cmd,"SET_SPEED", 9)==0) {
    int spd = atoi(cmd+10); //"SET_SPEED 120"
    MOTOR_SetSpeed(spd);  
    UART_Write("OK: Speed set\n");
  }
}
