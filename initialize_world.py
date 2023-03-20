import numpy as np
from world import World
from agents import Car, RectangleBuilding, Pedestrian, Painting
from geometry import Point
import time
import random

def configure_stoplights(): # whether stoplight for our agent is green or red
    rand = random.randint(0, 1)
    if rand == 0:
        return "vertical"
    else:
        return "horizontal"
"""
def initialize_pedestrians(w, n_peds=random.randint(1, 10)):
    peds = []
    ped_locs = []
    location = ["bottom-left", "bottom-right", "left-top", "left-bottom", "right-top", "right-bottom", 
                "top-left", "top-right"]
    speed = 1.3
    for i in range(n_peds):
        loc = location[random.randint(0, 7)]
        most_recent_ped = None
        if loc in ped_locs:
            most_recent_ped = max(idx for idx, val in enumerate(ped_locs) if val == loc)
            most_recent_ped = peds[most_recent_ped]
        if loc == "bottom-right":
            if most_recent_ped is not None:
"""
def execute(w, cars, car_locs):
    if random.random() < 0.25:
        task = "left"
    else: 
        task = "straight/right"
def initialize_agent(w, cars, car_locs):
    most_recent_car = None
    if "bottom" in car_locs:
        most_recent_car = max(idx for idx, val in enumerate(car_locs) if val == "bottom")
        most_recent_car = cars[most_recent_car]
    if most_recent_car is not None:
        new = most_recent_car.y - random.randint(16, 42)
        if new < 0:
            new = 0
        agent = Car(Point(65.25, new), np.pi / 2, "red")
    else:
        agent = Car(Point(65.25, random.randint(0, 25)), np.pi / 2, "red")
    w.add(agent)
    return agent

def initialize_cars(w, n_cars=random.randint(0, 10)):
    cars = []
    car_locs = []
    location = ["bottom-left", "bottom-right", "left-top", "left-bottom", "right-top", "right-bottom", 
                "top-left", "top-right"]
    for i in range(n_cars):
        loc = location[random.randint(0, 7)]
        most_recent_car = None
        distance_between = random.randint(8, 21)
        if loc in car_locs:
            most_recent_car = max(idx for idx, val in enumerate(car_locs) if val == loc)
            most_recent_car = cars[most_recent_car]
        if loc == "bottom-right":
            if most_recent_car is not None:
                if most_recent_car.y >= 22:
                    new = most_recent_car.y - distance_between
                    if new < 0:
                        new = 0
                    car = Car(Point(65.25, new), np.pi / 2, "blue")
            else:
                car = Car(Point(65.25, 42), np.pi / 2, "blue")
        elif loc == "bottom-left":
            if most_recent_car is not None:
                if most_recent_car.y <= 26:
                    new = most_recent_car.y + 8
                    if new > 40:
                        new = 40
                    car = Car(Point(55.25, new), 3*np.pi/2, "blue")
            else:
                car = Car(Point(55.25, 40), 3*np.pi/2, "blue")
        elif loc == "left-bottom":
            if most_recent_car is not None:
                if most_recent_car.x >= 22:
                    new = most_recent_car.x - distance_between
                    if new < 0:
                        new = 0
                    car = Car(Point(new, 55.25), 0, "blue")
            else:
                car = Car(Point(42, 55.25), 0, "blue")
        elif loc == "left-top":
            if most_recent_car is not None:
                if most_recent_car.x <= 26:
                    new = most_recent_car.x - 8
                    if new > 40:
                        new = 40
                    car = Car(Point(new, 65.25), np.pi, "blue")
            else:
                car = Car(Point(random.randint(0, 40), 65.25), np.pi, "blue")
        elif loc == "right-top":
            if most_recent_car is not None:
                if most_recent_car.x <= 98:
                    new = most_recent_car.x + distance_between
                    if new > 120:
                        new = 120
                    car = Car(Point(new, 65.25), np.pi, "blue")
            else:
                car = Car(Point(78, 65.25), np.pi, "blue")
        elif loc == "right-bottom":
            if most_recent_car is not None:
                if most_recent_car.x >= 86:
                    new = most_recent_car.x - 8
                    if new < 80:
                        new = 80
                    car = Car(Point(new, 55.25), 0, "blue")
            else:
                car = Car(Point(random.randint(80, 120), 65.25), 0, "blue")
        elif loc == "top-left":
            if most_recent_car is not None:
                if most_recent_car.y <= 98:
                    new = most_recent_car.y + distance_between
                    if new > 120:
                        new = 120
                    car = Car(Point(55.25, new), 3*np.pi/2, "blue")
            else:
                car = Car(Point(55.25, 78), 3*np.pi/2, "blue")
        else:
            if most_recent_car is not None:
                if most_recent_car.y >= 86:
                    new = most_recent_car.y - 8
                    if new < 80:
                        new = 80
                    car = Car(Point(65.25, new), np.pi/2, "blue")
            else:
                car = Car(Point(65.25, random.randint(80, 120)), np.pi/2, "blue")
        w.add(car)
        cars.append(car)
        car_locs.append(loc)
    agent = initialize_agent(w, cars, car_locs)
    return agent, cars, car_locs

def initialize_intersection(w: World):
    # sidewalks
    w.add(Painting(Point(95, 25), Point(50, 50), 'gray80'))
    w.add(Painting(Point(25, 25), Point(50, 50), 'gray80'))
    w.add(Painting(Point(95, 95), Point(50, 50), 'gray80'))
    w.add(Painting(Point(25, 95), Point(50, 50), 'gray80'))

    # buildings
    w.add(RectangleBuilding(Point(97.5, 97.5), Point(45, 45)))
    w.add(RectangleBuilding(Point(22.5, 22.5), Point(45, 45)))
    w.add(RectangleBuilding(Point(22.5, 97.5), Point(45, 45)))
    w.add(RectangleBuilding(Point(97.5, 22.5), Point(45, 45)))

    # vertical dividers
    w.add(Painting(Point(59, 22), Point(1, 44), '#f7d133'))
    w.add(Painting(Point(61, 22), Point(1, 44), '#f7d133'))
    w.add(Painting(Point(59, 98), Point(1, 44), '#f7d133'))
    w.add(Painting(Point(61, 98), Point(1, 44), '#f7d133'))

    #horizontal dividers
    w.add(Painting(Point(22, 59), Point(44, 1), '#f7d133'))
    w.add(Painting(Point(22, 61), Point(44, 1), '#f7d133'))
    w.add(Painting(Point(98, 59), Point(44, 1), '#f7d133'))
    w.add(Painting(Point(98, 61), Point(44, 1), '#f7d133'))

    # pedestrian crossings
    for i in range(9):
        #horizontal
        w.add(Painting(Point(52 + (2 * i), 47.5), Point(1, 4), "white"))
        w.add(Painting(Point(52 + (2 * i), 72.5), Point(1, 4), 'white'))
        #vertical
        w.add(Painting(Point(47.5, 52 + (2 * i)), Point(4, 1), 'white'))
        w.add(Painting(Point(72.5, 52 + (2 * i)), Point(4, 1), 'white'))
    return initialize_cars(w)

if __name__ == "__main__":
    human_controller = False
    dt = 0.1 # time steps in terms of seconds. In other words, 1/dt is the FPS.
    w = World(dt, width = 120, height = 120, ppm = 6) # The world is 120 meters by 120 meters. ppm is the pixels per meter.
    lights = configure_stoplights() 
    initialize_intersection(w)
    w.render()
    time.sleep(100)
    
    