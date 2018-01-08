package main

import (
	"fmt"
	"time"
)


/*
冒泡排序： 数值大的向后冒
 */
func maxBubble(array []int) (int64, []int) {
	start := time.Now().UnixNano()
	/*
	外层循环，反向遍历所有元素
	 */
	for i := len(array) - 1; i >= 0; i-- {
		/*
		内层循环，遍历 0 ~ (i - 1)
		从前往后，每次比较出最大的数字，冒泡（排到最后）
		 */
		for j := 0; j < i; j++ {
			if array[j] > array[j + 1] {
				array[j], array[j + 1] = array[j + 1], array[j]
			}
		}
	}
	end := time.Now().UnixNano()
	return end - start, array
}


/*
冒泡排序： 数值小的向前冒
 */
func minBubble(array []int) (int64, []int) {
	start := time.Now().UnixNano()
	/*
	外层循环，遍历所有元素
	 */
	for i := 0; i < len(array); i++ {
		/*
		内层循环，反向遍历 0 ~ (i - 1)
		从后往前，每次比较出最小的数字，冒泡（排到最后）
		 */
		for j := len(array) - 1; j > i; j-- {
			if array[j] < array[j - 1] {
				array[j], array[j - 1] = array[j - 1], array[j]
			}
		}
	}
	end := time.Now().UnixNano()
	return end - start, array
}


/*
快速排序
选取一个枢轴值，一趟排序后，将待排序列分成两部分，左边部分均不大于这个枢轴值，右边部分均不小于这个枢轴值
然后再次对两侧进行快速排序，直至整个序列有序
分治算法，原地排序
不稳定排序
https://www.cnblogs.com/ahalei/p/3568434.html
 */
func quick(array []int, args ...int) []int {
	var left, right int
	if len(args) > 0{
		left = args[0]
		right = args[1]
	} else {
		left = 0
		right = len(array) - 1
	}
	temp := array[left]
	if left < right {
		low := left
		high := right
		for high > low {
			// 从右边找一个比临时变量小的数，找到就交换
			for low < high && array[high] >= temp {
				high --
			}
			array[low] = array[high]
			// 从左边找一个比临时变量大的数，找到就交换
			for low < high && array[low] <= temp {
				low ++
			}
			array[high] = array[low]
		}
		array[low] = temp
		if left < low - 1 {
			quick(array, left, low - 1)
		}
		if low + 1 < right {
			quick(array, low + 1, right)
		}
	}
	return array
}


func main() {
	fmt.Println(maxBubble([]int{2, 56, 6, 10, 3, 56, 9, 12}))
	fmt.Println(minBubble([]int{2, 56, 6, 10, 3, 56, 9, 12}))
	fmt.Println(quick([]int{2, 56, 6, 10, 3, 56, 9, 12}))
}
