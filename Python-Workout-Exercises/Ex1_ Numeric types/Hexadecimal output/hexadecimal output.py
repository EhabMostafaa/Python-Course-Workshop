
def hex_converting(hex_number):
    dec_num=0
    for power,digit in enumerate(reversed(hex_number)):
        dec_num+= int(digit,16) *(16**power)
    return dec_num 

   
print(hex_converting("C"))