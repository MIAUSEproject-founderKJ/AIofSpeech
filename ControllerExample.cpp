// controller.cpp
//Opens serial port to MCU.
//Sends "SET_SPEED 120\n".
//The firmware reads this, updates motor speed, and replies with "OK: Speed set".

#include <iostream>
#include <fstream>
#include <string>
#include <thread>
#include <chrono>
#ifdef _WIN32
#include <windows.h>
#else
#include <fcntl.h>
#include <termios.h>
#include <unistd.h>
#endif

int main() {
  std::string port = "COM3"; // or "/dev/ttyUSB0" on Linux

  #ifdef _WIN32
  HANDLE hSerial = CreateFile(port.c_str(), GENERIC_READ | GENERIC_WRITE, 0,0, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0);

  if (hSerial == INVALID_HANDLE_VALUE){
    std::cerr<<"Error opening serial port.\n";
    return 1;
  }

  DWORD bytesWritten;
  std::string cmd="SET_SPEED 120\n";
  WriteFile(hSerial, cmd.c_str(), cmd.size(), &bytesWritten, NULL);
  std::cout << "Command sent:"<<cmd;
  CloseHandle(hSerial);

  #else 
    int fd = open(port.c_str(), O_RDWR | O_NOCTTY);
    struct termios tty;
    tcgetattr(fd, &tty);
    cfsetospeed(&tty, B115200);
    cfsetispeed(&tty, B115200);
    tcsetattr(fd, TCSANOW, &tty);

    std::string cmd = "SET_SPEED 120\n";
    write(fd, cmd.c_str(), cmd.size());
    std::cout << "Command sent: " << cmd;

    close(fd);
#endif

    return 0;
  
}
