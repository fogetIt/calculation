/*
* @Date:   2017-12-20 21:40:53
* @Last Modified time: 2017-12-20 21:40:55
*/
'use strict';


function maxBubble(arr) {
    const time = process.hrtime();
    for(let i = arr.length - 1; i >=0; i--) {
        for(let j = 0; j < i; j++) {
            if(arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
            }
        }
    }
    const diff = process.hrtime(time);
    return [diff[0] * Math.pow(10, 9) + diff[1], arr]
}


function minBubble(arr) {
    const time = process.hrtime();
    for(let i = 0; i < arr.length - 1; i++) {
        for(let j = arr.length - 1; j > i; j--) {
            if(arr[j] < arr[j - 1]) {
                [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]]
            }
        }
    }
    const diff = process.hrtime(time);
    return [diff[0] * Math.pow(10, 9) + diff[1], arr]
}


function quick(arr, left=0, right=arr.length - 1) {
    if(left < right) {
        let temp = arr[left];
        let low = left;
        let high = right;
        while(low < high) {
            while(high > low && arr[high] >= temp) {
                high --
            }
            arr[low] = arr[high];
            while(low < high && arr[low] <= temp) {
                low ++
            }
            arr[high] = arr[low]
        }
        arr[low] = temp;
        if(left < low - 1) {
            quick(arr, left, low - 1)
        }
        if(low + 1 < right) {
            quick(arr, low + 1, right)
        }
    }
    return arr;
}


console.log(maxBubble([2, 56, 6, 10, 3, 56, 9, 12]));
console.log(minBubble([2, 56, 6, 10, 3, 56, 9, 12]));
console.log(quick([2, 56, 6, 10, 3, 56, 9, 12]));