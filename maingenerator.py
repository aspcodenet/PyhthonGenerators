from dataclasses import dataclass
from time import sleep

# IDAG BYGGER Vi EN FABRIK 
# SOM SKAPAR 1000000 burkar soppa om dagen
@dataclass
class CanOfSoup:
    Created: bool
    Label:  bool
    Soup: bool

 # CREATE = Generator 
 # YIELD = puttar ut EN på löpande bandet
 # ger kontrollen tillbaka till den som anropade funkionen
 # i nästa varv i loopen kommer Create komma ihpg var den slutade
 # och fortsätta därifrån
  
def Create(n):
    for x in range(0,n):
        sleep(3) # 1
        yield CanOfSoup(True,False,False)

def PutOnLabel(canOfSoup):
    canOfSoup.Label = True
def PourSoup(canOfSoup):
    canOfSoup.Soup  = True

# VARJE VARV I LOOPEN 
# drar fram en till YIELD från Create        
for x in Create(100000000):
    PutOnLabel(x)
    PourSoup(x)
    print(x)



