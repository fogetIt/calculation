/*
* @Date:   2017-12-28 18:48:58
* @Last Modified time: 2017-12-28 18:49:00
*/
package main

import (
	"fmt"
	"strconv"
)


func zip(data string) (result string) {
	num := 1
	for i := 1; i < len(data); i ++ {
		if data[i] == data[i - 1] {
			num ++
		} else {
			result += string(data[i - 1])
			result += string(num)
			num = 1
		}
		if i == len(data) - 1 {
			result += string(data[i - 1])
			result += strconv.Itoa(num)
		}
	}
	return
}

func unzip(data string) (result string) {
	result = ""
	for i := 0; i < len(data); i ++ {
		if i % 2 == 1 {
			x, _ := strconv.Atoi(string(data[i]))
			for j := 0; j < x; j ++ {
				result += string(data[i - 1])
			}
		}
	}
	return
}

func betterZip(data string) (result string) {
	num := 1
	result = ""
	for i := 1; i < len(data); i ++ {
		if data[i] == data[i - 1] {
			num ++
		} else {
			result += string(data[i - 1])
			if num > 1 {
				result += string(num)
			}
			num = 1
		}
		if i == len(data) - 1 {
			result += string(data[i - 1])
			if num > 1 {
				result += string(num)
			}
		}
	}
	return
}


func main()  {
	fmt.Println(zip("aabaaccdfffgtjkii"))
	fmt.Println(unzip("a2b1a2c2d1f3g1t1j1k1i2"))
	fmt.Println(betterZip("aabaaccdfffgtjkii"))
}
