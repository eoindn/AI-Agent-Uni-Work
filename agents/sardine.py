
from model.agent import Agent

class Sardine(Agent):
    def __init__(self,x,y,name = "sardine",speed = 10):
        super().__init__(x,y,symbol = "S" , name= name)
        