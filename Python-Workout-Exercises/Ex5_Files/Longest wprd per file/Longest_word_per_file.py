import os

 
def find_longest_word(file_name):
    file=open(file_name,'r',encoding='utf-8')
    max_length=0
    max_word=""    
    for line in file.readlines():
        words=line.split()
        for word in words:
            # print(word)

            if len(word)>max_length:
                max_length=len(word)
                max_word=word
    max={max_word:max_length}
    return(max)               



def find_all_longest_words(files_directory):
    all_words={}
    file_paths=[]        
    print(os.listdir(files_directory))
    for files in os.listdir(files_directory):
        file_paths.append(os.path.join(files_directory, files))

    print(file_paths)
    for file2 in file_paths:
        all_words.update(find_longest_word(file2))
    return all_words

print(find_all_longest_words("files/"))





