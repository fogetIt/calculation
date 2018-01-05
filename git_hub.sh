#!/bin/bash
# @Date:   2018-01-05 13:33:50
# @Last Modified time: 2018-01-05 13:36:34
git status | grep "nothing to commit" >nul
echo $?
# git add --all
# git commit -m $now
# git pull origin master
# git push origin master