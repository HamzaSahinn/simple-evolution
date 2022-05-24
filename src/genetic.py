import math
from agent import Agent
from typing import List
import random


class Genetic:
    
    def __init__(self, agent_count):
        self.population_count = agent_count
        self.generation_dict = {}
        self.generation = 1
    
    
    def evolve(self, agent_list:List[Agent], mutation_rate, x_max, y_max):
        
        # LOG CURRENT GENERATION
        self._calc_stats_of_generation(agent_list)
        
        # GET SURVIVED AGENTS
        survived_agents = []
        for agent in agent_list:
            if agent.fitness >= agent.energy_need and agent.age < 7:
                survived_agents.append(agent)
        
        new_agents = []
        # CREATE NEXT GENERATION
        for index in range(1, len(agent_list), 2):
            agent_1 = agent_list[index]
            agent_2 = agent_list[index-1]
            
            crossover_weight = random.random()
            speed_new = (crossover_weight * agent_1.speed) + ((1 - crossover_weight) * agent_2.speed)
            field_new = (crossover_weight * agent_1.sensing_field_radius) + ((1 - crossover_weight) * agent_2.sensing_field_radius)
            
            mutate = random.random()
            if mutate <= mutation_rate:
                speed_new = speed_new * random.uniform(0.9,1.15)
                field_new = field_new * random.uniform(0.9,1.15)
            
            new_agents.append(Agent(x_max, y_max, speed=speed_new, field=field_new))
        
        self.generation += 1
        
        survived_agents.extend(new_agents)
        self.population_count = len(survived_agents)
        
        return survived_agents

        
    def _calc_stats_of_generation(self, agent_list: List[Agent]):
        if len(agent_list) < 1:
            return
        stat_dict = {}
        stat_dict["sum"] = 0
        stat_dict["best"] = agent_list[0]
        stat_dict["fitness_average"] = 0
        stat_dict["population"] = len(agent_list)
        
        speed = 0
        field = 0
        
        for agent in agent_list:
            stat_dict["sum"] += agent.fitness
            
            speed += agent.speed
            field += agent.sensing_field_radius
            
            if stat_dict["best"].fitness < agent.fitness:
                stat_dict["best"] = agent
        
        
        stat_dict["fitness_average"] = round(stat_dict["sum"] / stat_dict["population"], 2)
        stat_dict["avg_speed"] = round(speed / stat_dict["population"],2)
        stat_dict["avg_field"] = round(field / stat_dict["population"],2)
        
        self.generation_dict[self.generation] = stat_dict