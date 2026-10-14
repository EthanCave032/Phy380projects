#!/bin/bash
if [ $# == 0 ]
then
  echo "You have not provided any arguments. You
  must provide at least 1!"
  echo "filetest.sh"
  echo "Usage: filetest.sh filename1 [filename2,filename3,...]"
  echo " "
else
  for file in $*; do
      echo "Testing to see if $file exists..."
      if [ -e "$file" ]; then
	  comment="$file exists!"

	  permissions=$(ls -ld -- "$file" | awk '{print $1}')
	  echo "Permissions: " "$permissions"

	  if [ -f "$file" ]; then
	      if [ ! -s "$file" ]; then
		  echo "$file is empty."
	      fi
	  fi
	  
      else
	  comment="Sorry, $file does not exist"

      fi

      if [ -d "$file" ]; then
	  comment2="and it is a directory"

      else
	  comment2=""
  
                                                             
      fi
      echo "$comment $comment2"
      echo " "
  done
fi
