from dataclasses import dataclass
from time import sleep

# IDAG BYGGER Vi EN FABRIK 
# SOM SKAPAR 1000000 burkar soppa om dagen
@dataclass
class CanOfSoup:
    Created: bool
    Label:  bool
    Soup: bool


# Lista = []  - alla saker finns i minnet 
#             möjlighet att läsa framåt + bakåt + 
#               random access 18, 99
massa = [CanOfSoup(True,False,False) for x in range(0,100)]
print(massa)
for x in massa:
    print(x)

for index in range(len(massa)-1,0,-1):   
    print(massa[index])
print(massa[45])    

massa = (CanOfSoup(True,False,False) for x in range(0,100))
for x in massa:
    print(x)



 # CREATE = Generator 
 # YIELD = puttar ut EN på löpande bandet
 # ger kontrollen tillbaka till den som anropade funkionen
 # i nästa varv i loopen kommer Create komma ihpg var den slutade
 # och fortsätta därifrån
  
def Create(n):   # Jag var på yield raden och x = 1
    for x in range(0,n): # x = 1
        sleep(3) 
        yield CanOfSoup(True,False,False)

def PutOnLabel(canOfSoup):
    canOfSoup.Label = True
def PourSoup(canOfSoup):
    canOfSoup.Soup  = True

# VARJE VARV I LOOPEN 
# drar fram en till YIELD från Create    
# 
for x in Create(100000000):
    PutOnLabel(x)
    PourSoup(x)
    print(x)




for x in range(0,10000000):
    x = CanOfSoup(True,False,False)
    PutOnLabel(x)
    PourSoup(x)
    print(x)




