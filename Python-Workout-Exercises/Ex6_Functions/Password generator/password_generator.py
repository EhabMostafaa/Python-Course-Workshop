import random

def create_password_generator(characters):
    def create_password(length):
        sequence=[]
        for i in range (length):
            sequence.append(random.choice(characters))
        return ''.join(sequence)
    return create_password   

characters_password=create_password_generator('aksfascwq')
special_password=create_password_generator('#@!$^&(*)')

print(characters_password(5))
print(special_password(5))
