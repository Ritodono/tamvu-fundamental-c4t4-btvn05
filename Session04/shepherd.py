print("Hello, my name is Tam and these are my sheeps sizes")
size = (5, 7, 300, 90, 24,50, 75)
print(*size, sep =",")

print("Now my biggest sheep has size",max(size),"let's shear it")

print("After sheering, here is my flock")
print(5, 7, 8, 90, 24, 50, 75)
for i in range(3):
    print("Month {0}".format(size))
    print("One month has passed , now here is my flock")
    new_sheep = [x+50 for x in size]
    print (new_sheep)

    max_sheep = max(new_sheep)
    print ("Now my biggest sheep has size", max(new_sheep), "let's shear it")

    print ("After shearing, here is my flock: ")
    index = new_sheep.index(max(new_sheep))
    new_sheep[index] = 8
    print (new_sheep)
    

m = max(size)
print("Now my biggest sheep size",m,"let's shear it")

print("My flock has size in total: ", size)
print("I would get", size, "* 2$ = ", size *2, "$")
