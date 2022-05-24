from random import uniform
from typing import List
from food import Food

class Agent:
    
    def __init__(self, x_max, y_max, speed_max=2, field_max=5, speed=None, field=None, name=None):
        # POSITION OF AGENT
        self.x = uniform(0, x_max)
        self.y = uniform(0, y_max)
        
        # DNA OF AGENT 
        self.speed                  = uniform(0.1,speed_max)
        self.sensing_field_radius   = uniform(2, field_max)
        self.energy_need = self.speed + self.sensing_field_radius
        
        if speed is not None:
            self.speed = speed
        if field is not None:
            self.sensing_field_radius = field
        
        # PROPERITIES
        self.fitness = 0
        self.age = 1
        self.name = name
    
    def move(self, foods:List[Food]):
        best_food = self.sense(foods)
        
        # TEHERE IS NO FOOD IN SENSING FIELD
        if best_food is None:
            self.x += uniform(-1*self.speed, self.speed)
            self.y += uniform(-1*self.speed, self.speed)
        
        # FOOD IN SENSING FIELD
        else:
            best_food, index = best_food
            # ARRANGE NEW X
            if best_food.x - self.x <= 0:
                if self.x - best_food.x < self.speed:
                    self.x  = best_food.x
                else:
                    self.x -= self.speed 
            
            else:
                if best_food.x - self.x < self.speed:
                    self.x  = best_food.x
                else:
                    self.x += self.speed
            
            # ARRANGE NEW Y
            if best_food.y - self.y <= 0:
                if self.y - best_food.y < self.speed:
                    self.y  = best_food.y
                else:
                    self.y -= self.speed 
            
            else:
                if best_food.y - self.y < self.speed:
                    self.y  = best_food.y
                else:
                    self.y += self.speed  
    
    def sense(self, foods:List[Food]):
        closest_food_distance = 1000
        closest_food :List[Food, int]= None
        
        for index, food in enumerate(foods):
            x_max, x_min = self.x + self.sensing_field_radius, self.x - self.sensing_field_radius
            y_max, y_min = self.y + self.sensing_field_radius, self.y - self.sensing_field_radius
            
            if (x_min < food.x and x_max > food.x) and (y_min < food.y and y_max > food.y):
                distance = ((food.x - self.x)**2 + (food.y -self.y)**2)**0.5
        
                if distance < closest_food_distance:
                    closest_food_distance = distance
                    closest_food = [food, index]

        return closest_food
    
    def eat(self, foods:List[Food]):
        closest_food= self.sense(foods)
        if closest_food is None:
            pass
                
        elif closest_food[0].x == self.x and closest_food[0].y == self.y:
            self.fitness += closest_food[0].benefit
            del foods[closest_food[1]]
        
        return foods
    
    