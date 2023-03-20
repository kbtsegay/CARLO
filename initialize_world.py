import numpy as np
from world import World
from agents import Car, RectangleBuilding, Pedestrian, Painting
from geometry import Point
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
def task_manager(cars, car_locs, stoplight):
    tasks = []
    if random.random() < 0.25:
        task = "left"
    else: 
        task = "straight/right"
    for i in range(len(cars)):
        if stoplight == "vertical" and cars[i].heading == np.pi/2 and car_locs[i] == "bottom-right":
            if task == "left":
                tasks.append("bottom->left")
            else:
                if random.random() < 0.5:
                    tasks.append("bottom->right")
                else:
                    tasks.append("straight")
        elif stoplight == "vertical" and cars[i].heading == 3*np.pi/2 and car_locs[i] == "top-left":
            if task == "left":
                tasks.append("top->right")
            else:
                if random.random() < 0.5:
                    tasks.append("top->left")
                else: 
                    tasks.append("straight")
        elif stoplight == "horizontal" and cars[i].heading == 0 and car_locs[i] == "left-bottom":
            if task == "left":
                tasks.append("left->top")
            else:
                if random.random() < 0.5:
                    tasks.append("left->bottom")
                else: 
                    tasks.append("straight")
        elif stoplight == "horizontal" and cars[i].heading == np.pi and car_locs[i] == "right-top":
            if task == "left":
                tasks.append("right->bottom")
            else:
                if random.random() < 0.5:
                    tasks.append("right->top")
                else: 
                    tasks.append("straight")
        else:
            tasks.append("stay")
            
    return tasks

def execute(cars, tasks, stoplight):
    for i in range(len(cars)):
        if (tasks[i] == "bottom->left" and cars[i].y >= 52) or (tasks[i] == "left->top" and cars[i].x >= 52) or (tasks[i] == "top->right" and cars[i].y <= 68) or (tasks[i] == "right->bottom" and cars[i].x <= 68):
            cars[i].set_control(0.28, 1)
        elif (tasks[i] == "top->left" and cars[i].y <= 73) or (tasks[i] == "bottom->right" and cars[i].y >= 47) or (tasks[i] == "right->top" and cars[i].x <= 73) or (tasks[i] == "left->bottom" and cars[i].x >=47):
            cars[i].set_control(-0.45, 1)
        if tasks[i] == "bottom->left" or tasks[i] == "top->left":
            if  np.pi - 0.2 <= cars[i].heading <= np.pi + 0.2:
                cars[i].heading = np.pi
                cars[i].set_control(0, 0.3)
        elif tasks[i] == "top->right" or tasks[i] == "bottom->right":
            if -0.2 <= cars[i].heading <= 0.2:
                cars[i].heading = 0
                cars[i].set_control(0, 0.3)
        elif tasks[i] == "left->top" or tasks[i] == "right->top":
            if np.pi/2 - 0.2 <= cars[i].heading <= np.pi/2 + 0.2:
                cars[i].heading = np.pi/2
                cars[i].set_control(0, 0.3)
        elif tasks[i] == "right->bottom" or tasks[i] == "left->bottom":
            if 3*np.pi/2 - 0.2 <= cars[i].heading <= 3*np.pi/2 + 0.2:
                cars[i].heading = 3*np.pi/2
                cars[i].set_control(0, 0.3)

def initialize_agent(w, cars, car_locs):
    most_recent_car = None
    speed = 13
    if "bottom" in car_locs:
        most_recent_car = max(idx for idx, val in enumerate(car_locs) if val == "bottom")
        most_recent_car = cars[most_recent_car]
    if most_recent_car is not None:
        new = most_recent_car.y - 32
        if new < 0:
            new = 0
        agent = Car(Point(65.25, new), np.pi / 2, "red")
    else:
        agent = Car(Point(65.25, 26), np.pi / 2, "red")
    w.add(agent)
    return agent

def initialize_cars(w, n_cars=random.randint(0, 10)):
    cars = []
    car_locs = []
    location = ["bottom-left", "bottom-right", "left-top", "left-bottom", "right-top", "right-bottom", 
                "top-left", "top-right"]
    stoplight = configure_stoplights()
    speed_limit = random.randint(10, 16)
    for i in range(n_cars):
        loc = location[random.randint(0, 7)]
        most_recent_car = None
        if loc in car_locs:
            most_recent_car = max(idx for idx, val in enumerate(car_locs) if val == loc)
            most_recent_car = cars[most_recent_car]
        if loc == "bottom-right":
            if most_recent_car is not None:
                if most_recent_car.y >= 22:
                    new = most_recent_car.y - 8
                    if new < 0:
                        new = 0
                    car = Car(Point(65.25, new), np.pi / 2, "blue")
            else:
                car = Car(Point(65.25, 42), np.pi / 2, "blue")
            if stoplight == "vertical":
                car.velocity = Point(0, speed_limit)
            else:
                car.velocity = Point(0, 0)
        elif loc == "bottom-left":
            if most_recent_car is not None:
                if most_recent_car.y <= 26:
                    new = most_recent_car.y + 8
                    if new > 40:
                        new = 40
                    car = Car(Point(55.25, new), 3*np.pi/2, "blue")
            else:
                car = Car(Point(55.25, 40), 3*np.pi/2, "blue")
            car.velocity = Point(0, -speed_limit)
        elif loc == "left-bottom":
            if most_recent_car is not None:
                if most_recent_car.x >= 22:
                    new = most_recent_car.x - 8
                    if new < 0:
                        new = 0
                    car = Car(Point(new, 55.25), 0, "blue")
            else:
                car = Car(Point(42, 55.25), 0, "blue")
            if stoplight == "vertical":
                car.velocity = Point(0, 0)
            else:
                car.velocity = Point(speed_limit, 0)
        elif loc == "left-top":
            if most_recent_car is not None:
                if most_recent_car.x <= 26:
                    new = most_recent_car.x - 8
                    if new > 40:
                        new = 40
                    car = Car(Point(new, 65.25), np.pi, "blue")
            else:
                car = Car(Point(random.randint(0, 40), 65.25), np.pi, "blue")
            car.velocity = Point(-speed_limit, 0)
        elif loc == "right-top":
            if most_recent_car is not None:
                if most_recent_car.x <= 98:
                    new = most_recent_car.x + 8
                    if new > 120:
                        new = 120
                    car = Car(Point(new, 65.25), np.pi, "blue")
            else:
                car = Car(Point(78, 65.25), np.pi, "blue")
            if stoplight == "vertical":
                car.velocity = Point(0, 0)
            else:
                car.velocity = Point(-speed_limit, 0)
        elif loc == "right-bottom":
            if most_recent_car is not None:
                if most_recent_car.x >= 86:
                    new = most_recent_car.x - 8
                    if new < 80:
                        new = 80
                    car = Car(Point(new, 55.25), 0, "blue")
            else:
                car = Car(Point(random.randint(80, 120), 55.25), 0, "blue")
            car.velocity = Point(speed_limit, 0)
        elif loc == "top-left":
            if most_recent_car is not None:
                if most_recent_car.y <= 98:
                    new = most_recent_car.y + 8
                    if new > 120:
                        new = 120
                    car = Car(Point(55.25, new), 3*np.pi/2, "blue")
            else:
                car = Car(Point(55.25, 78), 3*np.pi/2, "blue")
            if stoplight == "vertical":
                car.velocity = Point(0, -speed_limit)
            else:
                car.velocity = Point(0, 0)
        else:
            if most_recent_car is not None:
                if most_recent_car.y >= 86:
                    new = most_recent_car.y - 8
                    if new < 80:
                        new = 80
                    car = Car(Point(65.25, new), np.pi/2, "blue")
            else:
                car = Car(Point(65.25, random.randint(80, 120)), np.pi/2, "blue")
            car.velocity = Point(0, speed_limit)
        w.add(car)
        cars.append(car)
        car_locs.append(loc)
    agent = initialize_agent(w, cars, car_locs)
    cars.append(agent)
    car_locs.append("bottom-right")
    return agent, cars, car_locs, stoplight

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
    
    