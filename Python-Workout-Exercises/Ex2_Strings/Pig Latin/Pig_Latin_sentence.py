def Pig_latin(English_sentence):
    array_words=English_sentence.split()
   
    Latin_sentence=""
    for word in array_words:
        if(word[0] in "a e i o u"):
            Latin_word=word+"way"
        else: 
            Latin_word=word[1:]+word[0]+"ay"
        Latin_sentence=Latin_sentence+" "+Latin_word        
    return (Latin_sentence)    
    
            
print(Pig_latin("this is a test translation"))