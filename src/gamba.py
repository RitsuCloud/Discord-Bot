import random

user_data = {}

# main function gamba
def gamba(name, amount):
    if notRegister(name):
        return ("Please do !register command to get started")
    else:
        if amount > user_data[name]:
           return f'{name} you dont have enough credits'
        else:
            result = random.randrange(1, 11)
            if result > 7:
                user_data[name] += amount
                return f'{name} won!, now you have {user_data[name]} credtis'
            else:
                user_data[name] -= amount 
                if user_data[name] > 0:
                    return f'{name} lost!, now you have {user_data[name]} credtis'
                else:
                    temp = user_data[name]
                    user_data[name] = None
                    return f'{name} lost! and you a brokie now, now you have {temp} credtis'

# name of the player to register
def register(name):
    if not notRegister(name):
        return f'{name} have already registered!'
    else:
        user_data[name] = 1000
        return f'{name} is now registed! You have 1000 credits'

# check how much credits a play has
def check(name):
    if notRegister(name):
        return f'{name} has not been registered!'
    else:
        return f'{name} has {user_data[name]} credits'

# check if the player is registered
def notRegister(name):
    if name in user_data and user_data[name] == None or not name in user_data:
        return True
    else:
        return False
    
