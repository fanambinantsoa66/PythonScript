package main

import "fmt"

func main() {
  // Variables
  var version int = 1
  // Constants
  const name string = "Gopher"
  // Type inference (short declaration)
  x := 3.14

  fmt.Printf("version=%d, name=%s\n", version, name)
  fmt.Printf("x=%v, type=%T\n", x, x)
}
