# task3.py

# modifying something in the global scope

# global
enemies = 1


def increase_enemies():  # local function scope (the only local scope)
    global enemies # telling python that there is a global var somewhere
    # and that's what we are working with below. Without this, we can't
    # modify a global variable in a local scope, only reference it if not
    # shadowed. 
    enemies += 1  # creating a NEW variable in a local scope SHADOWS global
    print(f"enemies inside function: {enemies}")

    # the pythonic way though isn't to try to modify global variables, but
    # use the return keyword to mutate the var and return it in place of
    # its current value as in 
            # enemies = increase_enemies(enemies) , if this function returned
            #  return enemy+=1 or something like that.


increase_enemies()
print(f"enemies outside function: {enemies}")
