
def summing_numbers(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum 

   
print(summing_numbers(20,30,20.5,-5))