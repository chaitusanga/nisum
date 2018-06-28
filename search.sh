#!/bin/sh

#rm tasks.txt timeline.txt
task=()
myarray=()
i=0

index=0

cat abc.txt |  awk '{print $0}' | grep -v "\[Pipeline\]" | grep -v "git"> no_pipeline.txt

cat no_pipeline.txt | awk '{print $0}' | grep -A 3 -B 2 "\[zeus_creative_recycles\]" | grep -v "\--"> file_new.txt

while read line
do
	echo "$line"

	#myarray[$index]=$line
    
	# awk '/zeus_creative_recycles/p' $line >> new_search.txt

	# echo $index

	# grep "shell" ${myarray[$index]}
	# if [ $? -eq 0 ]; then 
	# 	task[$index]=`grep -A 2 "shell" ${myarray[$index]}` 
	# 	#| grep -v "\--" | grep -v "shell"`
	# fi
	
	# index=$(expr $index + 1)

		#let i+=1
	#fi

	#echo "-------------$line---------------"
	#grep -n "shell" $line >> output.txt

	if [ `grep -q "zeus_creative_recycles" $line` ]; then
		task[$i]=`grep -A 1 "zeus_creative_recycles" $line | grep -v "\--"` 
		let i+=1
	fi
	#| grep -v "shell" | awk -F" " '{print $5 "\t" $6}'`
	#echo "$task \n" >> tasks.txt

		#date_time=`grep -A 1 venv $line | grep -v venv | grep -v "\--" | awk -F" " '{print $0}'`
		#echo "$date_time" >> timeline.txt
done < "file_new.txt"


for n in "${task[@]}";
do
	echo $n
done

#while read line
#do
#	date_time=`grep -A 1 venv $line | grep -v venv | grep -v "\--" | awk -F" " '{print $0}'`
#	echo "$date_time" >> timeline.txt
#done < "file_new.txt"

