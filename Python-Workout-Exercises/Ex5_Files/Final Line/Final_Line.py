def get_final_line(file_name):
	file=open(file_name,'r')
	for line in file.readlines():
		pass
	return line	
 
	
	
print(get_final_line("text.txt"))