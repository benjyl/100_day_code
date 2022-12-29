from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) -> None:
        self.cars = []
        self.move_dist = STARTING_MOVE_DISTANCE
    
    def start(self):
        for i in range(40):
            self.cars.append(Car(x_pos=random.randrange(-300, 300, 50), move_dist=self.move_dist))
        
    
    def gen_cars(self):
        # if random.choices([False, True], weights=[0.9999, 0.0001]):
        self.cars.append(Car(move_dist=self.move_dist))
    
    def move(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -350:
                car.ht()
                self.cars.remove(car)
                
    def detect_collision(self, turtle):
        for car in self.cars:
            if abs(turtle.ycor() - car.ycor()) < 20 and car.distance(turtle) < 25:
                print("Collision detected")
                return False
        return True
    
    def level_up(self):
        for car in self.cars:
            car.speed_up()
        self.move_dist +=10
                      
    
class Car(Turtle):
    def __init__(self, x_pos=300, move_dist=STARTING_MOVE_DISTANCE) -> None:
        super().__init__()
        self.color(random.sample(COLORS,1))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.pu()
        
        self.goto(x=x_pos, y=random.randrange(-240, 240, 20))
        self.move_dist = move_dist
    
    def move(self):
        self.fd(self.move_dist)
    
    def speed_up(self):
        self.move_dist += MOVE_INCREMENT
    
