
Menu = {'sandwich': 10 , 'Tea': 7 , 'Salad': 9}

def Restaurant(dictionary):
    sum=0
    valid=True
    order=input("please give me your request :").strip()
    while valid:
        if order in dictionary:
            sum+=dictionary[order]
            order=input("what else :").strip()    
        else:
            valid=False
            print(f"you must pay {sum} for your orders")    
            
print(Restaurant(Menu))