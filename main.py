
from dataclasses import dataclass


# IDAG BYGGER Vi EN FABRIK 
# SOM SKAPAR 1000000 burkar soppa om dagen

@dataclass
class CanOfSoup:
    Created: bool
    Label: bool
    Soup: bool

def Create(n):
    items = []
    for x in range(0,n):
        items.append(CanOfSoup(True,False,False))
    return items

def PutLabelOn(lista):
    for x in lista:
        x.Label = True
    return lista

def PourSoup(lista):
    for x in lista:
        x.Soup = True
    return lista

store1 = Create(100)
store2 = PutLabelOn(store1)
store3 = PourSoup(store2)
for can in store3:
    print(f"Nu packas denna {can}")



