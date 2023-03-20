import random
import numpy as np
from agents import Car

class QLearningAgent:
    def __init__(self, agent: Car): 
        self.observation_radius = 50 # meters
        self.position = (round(agent.x, 1), round(agent.y, 1)) # rounding forces the state space for agent to be discrete
        self.observation_space =  # 120 x 120 grid to 0.1 precision
        self.action_space = [("steer", -0.8), ("steer", -0.6), ("steer", -0.4), ("steer", -0.2), 
                             ("steer", 0.0), ("steer", 0.2), ("steer", 0.4), ("steer", 0.6), ("steer", 0.8),
                             ("accelerate", 0), ("accelerate", 1), ("accelerate", 2), ("accelerate", 3)]
        self.discount_factor = 0.95
        self.Q = np.zeros(self.num_states, len(self.action_space))
        self.epsilon = 0.8 # probability of random arm
        self.decay = 0.9
        self.learning_rate = 0.1

    def get_action(self):
        # epsilon greedy method of choosing action
        # return random action with probability epsilon
        # otherwise, return greedy action
        epsilon_greedy = random.uniform(0, 1)
        if self.epsilon > epsilon_greedy:
            self.epsilon *= self.decay
            action = random.sample(self.action_space)
        else:
            action = np.max(self.Q[self.position,:])
        return action
    
    def get_reward(self, ):

     # update the Q matrix
    def update(self, s, a, r, s_prime):
        self.Q[s,a] = self.Q[s,a] + self.learning_rate * (r + self.discount_factor * max(self.Q[s_prime,:]) - self.Q[s,a])