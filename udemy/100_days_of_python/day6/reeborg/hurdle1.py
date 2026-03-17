def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for n in range(6):
    jump_hurdle()



