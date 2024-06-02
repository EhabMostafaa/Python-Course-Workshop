class Animal():
    def __init__(self, species, color, number_of_legs):
        self.species = species
        self.color = color
        self.number_of_legs = number_of_legs
    
    def __repr__(self):
        return f" {self.species} {self.color}, {self.number_of_legs} legs" 


def add_info(animal_name,Species,Color,Num_of_legs):
    animal_name=Animal(Species,Color,Num_of_legs)
    print(animal_name)    

    
add_info("wolf","wolf","brown",4)
add_info("horse","horse","white",4)
add_info("lion","lion","red",4)
add_info("snake","snake","black",0)
    
    
    

        