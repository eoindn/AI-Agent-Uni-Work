from model.agent import Agent



class Plankton(Agent):


    def __init__(self, x, y, name="Plankton", speed=1):
        super().__init__(x, y, symbol='p', name=name)  # Pass all required params
        self.speed = speed