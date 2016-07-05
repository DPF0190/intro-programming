#!/bin/bash
echo "enter first number"
read inp1
echo "enter the second number"
read inp2
echo "1. Add"
echo "2. Sub"
echo "3. Mult"
echo -n "please choose a word [1,2 or 3]?"
read oper
if [ $oper -eq 1 ]
then
	echo "addition result " $(($inp1 + $inp2))
else
	if [ $oper -eq 2 ]
	then
		echo "subtraction result " $(($inp1 - $inp2))
	else
		if [ $oper -eq 3 ]
		then
			echo "multiplication result "  $(($inp1 * $inp2))
	else
		echo "invalid input"
	fi
   fi
fi



