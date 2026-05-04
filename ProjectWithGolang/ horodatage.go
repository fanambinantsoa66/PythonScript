package main

import (
  "fmt"
  "time"
)

func main() {
  now := time.Now()
  year, week := now.ISOWeek()
  fmt.Println("Year:", now.Year())
  fmt.Printf("ISO week: %d-%02d\n", year, week)
}
