from random import uniform

class Food:
    
    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        
        # POSITION
        self.x = uniform(0, x_max)
        self.y = uniform(0, y_max)
        
        self.benefit = 1
    
    def respawn(self):
        self.x = uniform(0, self.x_max)
        self.y = uniform(0, self.y_max)
        
        self.benefit = 1