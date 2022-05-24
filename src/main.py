from agent import Agent
from food import Food
from typing import List
from genetic import Genetic


days = 141
food_num = 100
initial_agent_num = 20

mutation_rate = 0.2

max_x = 70
max_y = 70

agent_list:List[Agent]  = []
food_list:List[Food]    = []

genetic_object = Genetic(initial_agent_num)


# INITIALIZE AGENTS AND FOODS
for i in range(initial_agent_num):
     agent_list.append(Agent(max_x,max_y,2.5,10))

for day in range(1,days):
    food_list.clear()
    for i in range(food_num):
        food_list.append(Food(max_x,max_y))
    
    for agent in agent_list:
        agent.move(food_list)

    for agent in agent_list:
        food_list = agent.eat(food_list)
    
    if day % 7 == 0:
        agent_list = genetic_object.evolve(agent_list, mutation_rate, max_x, max_y)

for stat in genetic_object.generation_dict.values():
    print(stat, end="\n")