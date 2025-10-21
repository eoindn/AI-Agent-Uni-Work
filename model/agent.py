from model.location import Location
from abc import ABC, abstractmethod

class Agent(ABC):

    def __init__(self,x,y,symbol,name = "Agent"):
        self.y = y 
        self.x = x

        self.symbol = symbol
        self.name = name

        self.health = 100
        self.max_health = 100
        self.alive = True
        self.stamina = 100
        self.max_stamina = 100
        self.energy = 100

    def eat(self,ammout):
        if self.energy == 100:
            return "eaten"
        self.energy += ammout

    def get_position(self):
        return(self.x,self.y)
    
    def is_alive(self):
        return self.alive
    
    def __str__(self):

        status = "ALIVE" if self.alive else "DEAD"
        return f"{self.name} ({self.symbol}) at ({self.x}, {self.y}) - HP: {self.health}/{self.max_health} [{status}]"
    
    def __repr__(self):
        return f"Agent('{self.name}', pos=({self.x},{self.y}), hp={self.health})"


    
        








