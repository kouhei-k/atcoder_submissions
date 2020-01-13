package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	sc.Split(bufio.ScanWords)
	a := nextInt()
	b := nextInt()
	defer out.Flush()
	a *= b
	if a%2 == 0 {
		out.WriteString("Even")
	} else {
		out.WriteString("Odd")
	}
	out.Flush()
	fmt.Println()

}
func next() string {
	sc.Scan()
	return sc.Text()
}
func nextInt() int {
	a, e := strconv.Atoi(next())
	if e != nil {
		panic(e)
	}
	return a
}
