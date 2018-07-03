from random import randint
numb = randint(1,100)
playing = True
count = 0

while playing:
    guess =int(input("Guest my number(1-100)"))
    if guess > numb:
        print("Too large")
    elif guess < numb:
        print("Too small,:(")
    else:
        print("Bingo,:)")
        playing = False
        break
    count += 1 
    if count == 7:
        print("You lose!")
        playing = False




