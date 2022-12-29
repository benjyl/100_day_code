import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
car_manager = CarManager()
car_manager.start()

game_is_on = True
frames = 3
while game_is_on:
# for i in range(20):
    time.sleep(0.1)
    screen.update()
    
    if frames == 3:
        car_manager.gen_car()
        frames = 0
    car_manager.move()
    
    game_is_on = car_manager.detect_collision(player)
    
    if not game_is_on:
        screen.update()
        scoreboard.game_over()
    
    # increase level when turtle reaches top
    if player.ycor() > 280:
        player.new_level() # reset player to start
        scoreboard.update_level() # update scoreboard
        car_manager.level_up()
    
    frames +=1
    
    
    
screen.exitonclick()
