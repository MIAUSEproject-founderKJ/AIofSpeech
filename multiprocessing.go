package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// Function simulating microphone input
func listenMicrophone(q chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	for {
		time.Sleep(time.Duration(rand.Intn(1000)+500) * time.Millisecond)
		commands := []string{"turn on the light", "move forward", "stop"}
		text := commands[rand.Intn(len(commands))]
		fmt.Println("[Mic] Heard:", text)
		q <- text
	}
}

// Function processing commands
func processCommand(q chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	for text := range q {
		fmt.Println("[Processor] Executing command for:", text)
		time.Sleep(500 * time.Millisecond)
	}
}

// Background monitor
func backgroundMonitor(wg *sync.WaitGroup) {
	defer wg.Done()
	for {
		fmt.Println("[Monitor] System OK")
		time.Sleep(3 * time.Second)
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	q := make(chan string, 10) // buffered channel
	var wg sync.WaitGroup

	wg.Add(3)
	go listenMicrophone(q, &wg)
	go processCommand(q, &wg)
	go backgroundMonitor(&wg)

	// Let goroutines run for 10 seconds
	time.Sleep(10 * time.Second)

	fmt.Println("Terminating processes...")

	// Graceful shutdown
	close(q)

	// Optional: Wait for goroutines that finish when q is closed
	time.Sleep(1 * time.Second)
}
