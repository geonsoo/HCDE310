#!/bin/sh
if [ ! -e ~/CourseFiles ]; then
	cd ~
	mkDir CourseFiles
	cd ~/CourseFiles
	git init
	mkDir hcde310a16
	echo created intial directories
	echo
fi

cd ~/CourseFiles/hcde310a16

git pull git://git.assembla.com/hcde310a16.git
cd ~/CourseFiles/hcde310a16/Homeworks

if [ $# -eq 0 ]; then
	echo 
	echo fetched lectures and solutions
	#for hwfolder in *
	#do
	#	if [ ! -d ~/Homeworks/"$hwfolder" ]; then
	#		echo making directory ~/Homeworks/"$hwfolder"
	#		mkdir -p ~/Homeworks/"$hwfolder"
	#	fi
	#	cp -i -r "$hwfolder"/* ~/Homeworks/"$hwfolder"/     
	#done

	# Make another copy
	#for hwfolder in *
	#do
	#	if [ ! -d /home/me/Homeworks_OriginalVersion/"$hwfolder" ]; then
	#		echo making directory /home/me/Homeworks_OriginalVersion/"$hwfolder"
	#		mkdir -p /home/me/Homeworks_OriginalVersion/"$hwfolder"
	#	fi
	#	cp -f -r "$hwfolder"/* /home/me/Homeworks_OriginalVersion/"$hwfolder"/     
	#done

else 
	echo fetching homework "$1"
	
        if [ ! -d ~/Homeworks/hw"$1" ]; then
                echo making directory ~/Homeworks/hw"$1"
                mkdir -p ~/Homeworks/hw"$1"
        fi

      	if [ ! -d ~/Homeworks_OriginalVersion/hw"$1" ]; then
                echo making directory ~/Homeworks_OriginalVersion/hw"$1"
                mkdir -p ~/Homeworks_OriginalVersion/hw"$1"
        fi

	cp -i -r hw"$1"/* ~/Homeworks/hw"$1"/
	cp -f -r hw"$1"/* ~/Homeworks_OriginalVersion/hw"$1"/
fi