from world import World
from initialize_world import initialize_intersection, task_manager, execute
from qlearning import QLearningAgent

if __name__ == "__main__":
    human_controller = False
    dt = 0.1 # time steps in terms of seconds. In other words, 1/dt is the FPS.
    w = World(dt, width = 120, height = 120, ppm = 6) # The world is 120 meters by 120 meters. ppm is the pixels per meter.
    agent, cars, car_locs, stoplight, sidewalks, buildings = initialize_intersection(w)
    peds = []
    qlearning = QLearningAgent(agent, cars, peds, sidewalks, buildings)
    tasks = task_manager(cars, car_locs, stoplight)
    while True:
        execute(cars, tasks, stoplight)
        w.tick()
