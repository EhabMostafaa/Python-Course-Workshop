

def get_rainfall():
    exist_dict={}
    valid=True
    
    while valid:
        city=input("enter the city name or press enter to exit : ").strip()
        if city=="":
            valid=0
            break
        
        elif city not in exist_dict:
            value=int(input("enter the value : "))
            pairs={city:value}
            exist_dict.update(pairs)
        
        else:
            value=int(input("enter the value : "))
            new_value=int(exist_dict[city])+value
            pairs={city:new_value}
            exist_dict.update(pairs)
    
    print(exist_dict)

print(get_rainfall())
