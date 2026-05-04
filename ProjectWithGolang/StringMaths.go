package main

import (
  "fmt"
  "math"
  "strings"
)

func main() {
  s := "go, go, gopher"
  upper := strings.ToUpper(s)
  count := strings.Count(s, "go")
  r := math.Sqrt(49)

  fmt.Println(upper)
  fmt.Println("count go:", count)
  fmt.Println("sqrt(49):", r)
}
