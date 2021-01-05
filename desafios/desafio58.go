package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	fmt.Println("Pensei em um número entre 0 e 10 tente advinhar")
	var user int
	fmt.Scan(&user)
	counter := 0

	rand.Seed(time.Now().UnixNano())
	computer := rand.Intn(10)
	exit := true
	for exit == true {
		if user == computer {
			fmt.Printf("O computador colou %v e você %v você acertou\n", computer, user)
			counter++
			exit = false
		} else if user > computer {
			fmt.Println("O número é menor tente novamente de 0 até 10")
			fmt.Scan(&user)
		} else if user < computer {
			fmt.Println("O número é maior tente novamente de 0 até 10")
			fmt.Scan(&user)
		}
	}
}
