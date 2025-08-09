#!/bin/bash


regex1="^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}}$"
regex2="^([0-9]\{3\}) [0-9]\{3\}\-[0-9]\{4\}$"


# extending regex
grep -e "$regex1" -e "$regex2" file.txt