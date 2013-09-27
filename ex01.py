import os
import shutil 

#for i in range(0,25): 
#	os.mkdir(chr(i + 97))

# iterate through files and add them to the 
# correct directory
files_list = os.listdir("files")

for i in range(len(files_list)):
	shutil.move("files/" + files_list[i], files_list[i][0])


