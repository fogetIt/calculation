/*
 * @Date:   2017-12-19 17:54:44
 * @Last Modified time: 2017-12-20 21:42:00
 */
'use strict';


function straight(arr) {
    // HRT, 高精度计时 => [seconds, nanoseconds]
    const time = process.hrtime();
    for (var i = 0; i < arr.length; i++) {
        for (var j = i - 1; j >= 0 && arr[j] > arr[j + 1]; j--) {
            [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
        }
    }
    const diff = process.hrtime(time);
    return [diff[0] * Math.pow(10, 6) + diff[1], arr]
}


function DLShell(arr) {
    const time = process.hrtime();
    /*
    分组
     */
    for (var g = arr.length / 2; g > 0; g /= 2) {
        /*
        获取每组最后一个元素
         */
        for (var i = g; i < arr.length; i++) {
            /*
            把每个组进行直接插入排序
             */
            for (var j = i; j - g >= 0 && arr[j] < arr[j - g]; j -= g) {
                [arr[j], arr[j - g]] = [arr[j - g], arr[j]]
            }
        }
    }
    const diff = process.hrtime(time);
    return [diff[0] * Math.pow(10, 9) + diff[1], arr]
}


// go, js, python 都是引用传递
console.log(straight([2, 56, 6, 10, 3, 56, 9, 12]));
console.log(DLShell([2, 56, 6, 10, 3, 56, 9, 12]));