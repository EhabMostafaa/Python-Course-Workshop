def word_count(file_name):
    file = open (file_name,'r')
    line_count=0
    char_count=0
    unique_characters=set()
    for line in file.readlines():
        line_count+=1
        char_count+=len(line)
        unique_characters.update(line.split())
    print(len(unique_characters))    
    print("number of lines: "+str(line_count))
    print("number of characters: "+str(char_count))

word_count("wcfile.txt")
