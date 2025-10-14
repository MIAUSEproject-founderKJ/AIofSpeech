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
  else if (strncmp(cmd, "STOP", 4) == 0 ){
    MOTOR_Stop();
    UART_Write("ERR: Unknown command\n");
  }
}

int main(void) {
  UART_Init (115200);
  Motor_Init();

  char buffer[64];
  while (1) {
    if (UART_ReadLine(buffer, sizeof(buffer))){
      processCommand(buffer);
    }
  }
}
