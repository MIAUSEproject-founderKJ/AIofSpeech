package main

import (
	"fmt"
	"os"
	"os/exec"
	"time"
)

func main() {
	// List of commands to run as separate processes
	commands := []string{"process1", "process2", "process3"}

	var procs []*exec.Cmd

	for _, cmdName := range commands {
		// Here we assume process1, process2, process3 are executables in your PATH
		cmd := exec.Command(cmdName)
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr

		err := cmd.Start()
		if err != nil {
			fmt.Println("Error starting", cmdName, ":", err)
			continue
		}

		procs = append(procs, cmd)
		fmt.Println(cmdName, "started with PID", cmd.Process.Pid)
	}

	// Let them run for 10 seconds
	time.Sleep(10 * time.Second)

	fmt.Println("Terminating processes...")

	// Kill all processes
	for _, cmd := range procs {
		if cmd.Process != nil {
			cmd.Process.Kill()
		}
	}
}
