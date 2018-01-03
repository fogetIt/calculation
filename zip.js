/*
* @Date:   2017-12-28 18:48:51
* @Last Modified time: 2017-12-28 18:48:53
*/
'use strict';


function zip(data) {
    let num = 1;
    let result = '';
    for (let i = 1; i < data.length; i++) {
        if (data[i] === data[i - 1]) {
            num += 1
        } else {
            result += data[i - 1];
            result += num;
            num = 1;
        }
        if (i === data.length - 1) {
            result += data[i - 1];
            result += num;
        }
    }
    return result;
}


function unzip(data) {
    let result = '';
    for (let i = 0; i < data.length; i ++) {
        if (i % 2) {
            for (let j = 0; j < Number(data[i]); j ++) {
                result += data[i - 1];
            }
        }
    }
    return result;
}


function better_zip(data) {
    let num = 1;
    let result = "";
    for (let i = 1; i < data.length; i++) {
        if (data[i] === data[i - 1]) {
            num += 1
        } else {
            result += data[i - 1];
            if (num > 1) {
                result += num;
            }
            num = 1
        }
        if (i === data.length - 1) {
            result += data[i - 1];
            if (num > 1) {
                result += num;
            }
        }
    }
    return result;
}


console.log(zip('aabaaccdfffgtjkii'));
console.log(unzip('a2b1a2c2d1f3g1t1j1k1i2'));
console.log(better_zip('aabaaccdfffgtjkii'));
