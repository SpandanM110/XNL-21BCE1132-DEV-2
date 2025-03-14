package main

import (
	"fmt"
	"log"
	"net/http"
)

func analyticsHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Analytics data processed!")
}

func main() {
	http.HandleFunc("/analytics", analyticsHandler)
	log.Println("Go Analytics Service running on port 9000")
	log.Fatal(http.ListenAndServe(":9000", nil))
}
