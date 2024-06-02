def sum_numbers(strings):
    sum=0
    string_array=strings.split(" ")
    for element in string_array:
        if element.isdigit():
            sum+=int(element)
        else:
            print(f"{element} not digit") 
    return sum

print(sum_numbers('10 abc 20 das 30 44ds 40'))