import string

def repeated_letters(words_lists):
    
    for charater in words_lists:
        for letter in charater:
            if charater.count(letter)>1:
                
            
            
            converted=converted+charater
    return(converted)
   
print(repeated_letters(['this','is','elementary','test','example']))