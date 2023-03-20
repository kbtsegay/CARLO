import random
import numpy as np
from entities import Entity
from agents import Car, Pedestrian, RectangleBuilding, Painting
from world import World

class QLearningAgent:
    def __init__(self, agent: Car, cars: list[Car], peds: list[Pedestrian], sidewalks: list[Painting], 
                 buildings: list[RectangleBuilding]):
        self.cars = cars
        self.peds = peds
        self.sidewalks = sidewalks
        self.buildings = buildings
        self.observation_radius = 50 # meters
        self.agent = agent
        self.observation_space = np.zeros((810, 110)) # 81 x 51 grid to 0.1 precision. ie. 75m in front, and 5m on all sides of car
        self.action_space = [("steer", -0.8), ("steer", -0.6), ("steer", -0.4), ("steer", -0.2), 
                             ("steer", 0.0), ("steer", 0.2), ("steer", 0.4), ("steer", 0.6), ("steer", 0.8),
                             ("accelerate", 0), ("accelerate", 1), ("accelerate", 2), ("accelerate", 3)]
        self.discount_factor = 0.95
        self.Q = np.zeros(self.num_states, len(self.action_space))
        self.epsilon = 0.8 # probability of random arm
        self.decay = 0.9
        self.learning_rate = 0.1
    
    def in_observation_space(self, entity: Entity):
        if self.agent - 5 <= entity.x <= self.agent + 5 and self.agent - 5 <= entity.y <= self.agent + 75:
            return True
        else:
            return False

    def update_observations(self):
        self.observation_space = np.zeros((1010, 510))
        for car in self.cars:
            if self.agent - 5 <= car.x <= self.agent + 5 and self.agent - 5 <= car.y <= self.agent + 75:
                self.observation_space[(car.y * 10) - 1][(car.x * 10) - 1] = 1
        for ped in self.peds:
            if self.agent - 5 <= ped.x <= self.agent + 5 and self.agent - 5 <= ped.y <= self.agent + 75:
                self.observation_space[(ped.y * 10) - 1][(ped.x * 10) - 1] = 2
        
    def get_action(self):
        # epsilon greedy method of choosing action
        # return random action with probability epsilon
        # otherwise, return greedy action
        epsilon_greedy = random.uniform(0, 1)
        if self.epsilon > epsilon_greedy:
            self.epsilon *= self.decay
            action = random.sample(self.action_space)
        else:
            action = np.max(self.Q[self.observation_space,:])
        return action
    
    def get_reward(self):
        reward = 0
        for car in self.cars:
            if self.agent.collidesWith(car):
                reward -= 150
        for ped in self.peds:
            if self.agent.collidesWith(ped):
                reward -= 200
        for building in self.buildings:
            if self.agent.collidesWith(building):
                reward -= 100
        for sidewalk in self.sidewalks:
            if self.agent.collidesWith(sidewalk):
                reward -= 100
        for car in self.cars:
            if abs(car.x - self.agent.x) < 5 and 0 < car.y - self.agent.y
     # update the Q matrix
    def update(self, s, a, r, s_prime):
        self.Q[s,a] = self.Q[s,a] + self.learning_rate * (r + self.discount_factor * max(self.Q[s_prime,:]) - self.Q[s,a])