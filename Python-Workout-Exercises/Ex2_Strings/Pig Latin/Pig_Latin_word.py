def Pig_latin(English_word):
    if(English_word[0] in "a e i o u"):
        Latin_word=English_word+"way"
    else: 
        Latin_word=English_word[1:]+English_word[0]+"ay"
    return Latin_word        
    
    
            
print(Pig_latin("computer"))