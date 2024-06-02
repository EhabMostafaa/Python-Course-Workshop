class scoop():    
    def __init__(self,flavour):
        self.flavour=flavour

def create_scoops():
    scoops= [scoop('Chocolate'),
             scoop('vanilla'),
             scoop('mango')]
    
    for Scoop in scoops:
        print(Scoop.flavour)
        
create_scoops()