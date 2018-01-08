package main

import (
	"fmt"
	"time"
)


func straight(array []int) (int64, []int) {
	start := time.Now().UnixNano()
	/*
	从索引 1 开始循环，每次截取一个序列 array[0: i]
	 */
	for i := 1; i < len(array); i ++ {
		/*
		== 拿 array[j + 1] 从后向前与一个有序序列依次对比
		序列的每个元素同外层循环的`当前元素`（array[j + 1], array[i]）依次比对
		如果 array[j] > array[j + 1] ，交换位置

		// 写法1
		for ...; ... && array[j] > array[j + 1]; ... {
			当条件不满足，立即打断循环
		}
		// 写法2
		for ... {
			if array[j] > array[j + 1] {
				当条件不满足，跳过，继续循环
				加上 else {break} == 写法1
			}
		}
		 */
		for j := i - 1; j >= 0 && array[j] > array[j + 1]; j -- {
			array[j], array[j + 1] = array[j + 1], array[j]
		}
	}
	end := time.Now().UnixNano()
	return end - start, array
}


/*
先比较距离远的元素，而不是像简单交换排序算法那样先比较相邻的元素
这样可以快速减少大量的无序情况，从而减轻后续的工作
 */
func DLShell(array []int) (int64, []int) {
	start := time.Now().UnixNano()
	/*
	分组
	 */
	for g := len(array) / 2; g > 0 ; g /= 2 {
		/*
		获取每组最后一个元素
		 */
		for i := g; i < len(array); i++ {
			/*
			把每个组进行直接插入排序
			 */
			for j := i; j - g >= 0 && array[j] < array[j - g]; j -= g {
				array[j], array[j - g] = array[j - g], array[j]
			}
		}
	}
	end := time.Now().UnixNano()
	return end - start, array
}


/*
插入排序是稳定的
 */
func main() {
	fmt.Println(straight([]int{2, 56, 6, 10, 3, 56, 9, 12}))
	fmt.Println(DLShell([]int{2, 56, 6, 10, 3, 56, 9, 12}))
}
