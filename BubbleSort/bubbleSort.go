//bubble sort
//O(n^2) complexity
package main

import (
	"fmt"
)

func main() {
	array := []int{10,5,9,8,7,1,2,25,101}
	for i := 0; i < len(array); i++ {
		for j := i+1; j < len(array); j++ {
			if array[j] < array[i] {
				x := array[i]
				array[i] = array[j]
				array[j] = x
			}
		}
	}

	fmt.Println(array)
}
