#!/bin/bash
# @Date:   2018-01-05 13:33:50
# @Last Modified time: 2018-01-05 13:40:00
git status | grep 'nothing to commit \| 无文件要提交'
echo $?
# git add --all
# git commit -m $now
# git pull origin master
# git push origin master