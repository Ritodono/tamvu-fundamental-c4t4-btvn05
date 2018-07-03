from random import randint

mood = randint(0,100)

if mood < 30:
    print("I feel bad")
elif mood < 60:
    print("I feel ok")    
else:print("I'm good") 

