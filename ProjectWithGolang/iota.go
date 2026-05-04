package main

import "fmt"

func main() {
  // iota auto-increments constants: handy for enums
  const (
    Sunday = iota
    Monday
    Tuesday
  )
  fmt.Println(Sunday, Monday, Tuesday)
}
