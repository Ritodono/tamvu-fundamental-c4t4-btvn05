

item = ["T-shirt", "Sweater"]


while True:
    n = input("Welcome to our shop, what do you want(C, R, U, D)?")
    if n == "R":
        print("Our items: T-shirt, sweater")
    elif n == "C":
        create = input("Enter new item:")
        item.append(create)
        print("Our items:", *item, sep=",")
    elif n == "U":
        update = int(input("Update position:"))
        new = input("New item")
        item[update - 1]= new
        print("Our items:", *item, sep=",")
    elif n == "D":
        delete = int(intput("Delete position"))
        del item[2]
        print("Our items:", *item, sep=",")
    
    else:
        print("It's ok")
        break












