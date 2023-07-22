import random

user_data = {}

def numGussing(name, amount, num):
    if notRegister(name):
        return ("Please do !register command to get started")
    else:
        result = random.randrange(1,11)
        if amount > user_data[name]:
            return f'You not balling like that, keep the amount realistic!'
        if result == num:
            user_data[name] += amount * 19
            return(f'YOU GUESSED IT!!!!, now {name} have {user_data[name]} credits!')
        else:
            user_data[name] -= amount
            if zeroOrLess(name):
                return f'{name} lost! and you are out since you have no credits left!'
            else:
                return(f'Good try, but you failed, now {name} have {user_data[name]} credits!')

# main function gamba
def gamba(name, amount):
    if notRegister(name):
        return ("Please do !register command to get started")
    else:
        if amount > user_data[name]:
           return f'{name} dont have enough credits!'
        else:
            result = random.randrange(1, 11)
            if result > 7:
                user_data[name] += amount
                return f'{name} won!, now you have {user_data[name]} credits!'
            else:
                user_data[name] -= amount 
                if zeroOrLess(name):
                    return f'{name} lost! and you are out since you have no credits left!'
                else:
                    return f'{name} lost!, now you have {user_data[name]} credits!'

# name of the player to register
def register(name):
    if not notRegister(name):
        return f'{name} have already registered!'
    else:
        user_data[name] = 1000
        return f'{name} is now registered! You have 1000 credits!'

# check how much credits a play has
def check(name):
    if notRegister(name):
        return f'{name} has not been registered!'
    else:
        return f'{name} has {user_data[name]} credits!'

# check if the player is registered
def notRegister(name):
    if name in user_data and user_data[name] == None or not name in user_data:
        return True
    else:
        return False

def zeroOrLess(name):
    if user_data[name] <= 0:
        user_data[name] = None
        return True
    else:
        return False

# unit testing only
def clearData():
    user_data.clear()
