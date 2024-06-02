
def Ubbi_Dubbi(English_word):
    converted=""
    for charater in English_word:
        if(charater in "a e i o u"):
            converted=converted+"ub"+charater
        else:
            converted=converted+charater
    return(converted)
   
print(Ubbi_Dubbi("program"))