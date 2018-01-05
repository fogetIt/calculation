#!/bin/bash
# @Date:   2018-01-05 13:33:50
# @Last Modified time: 2018-01-05 13:49:22
git status | grep 'nothing to commit\|无文件要提交'
if [ $? != 0 ]; then
    now=$(date +%Y-%m-%d~%H:%M:%S)
    git add .
    git commit -m $now
    git pull origin master
    git push origin master
else
    git pull origin master
fi
echo "update successful"