

print("Hi there")
fav = ["death note", "netflix", "teaching"]
fav[0]="meat"
print("*"* 20)
for index,item in enumerate(fav):
    print(index + 1, item,sep ="." )

pos = int(input("Position you want to update:"))
update_fav = input("Your replacing fav:")
print(*fav,sep=",")
for index, item in enumerate(fav):
    print(index, item)
print("*"*20)
 
print(fav.append)


