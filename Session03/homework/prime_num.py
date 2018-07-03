
from random import randint
numb = randint(1,100)

if numb > 1:
    for i in range(2,numb):
        if (numb % i) == 0:
            print(numb,"is not a prime number")
            print(i,"times",numb//i,"is",numb)
            break
    else:
        print(numb,"is a prime number")
else:
    print(numb,"is not a prime number")

