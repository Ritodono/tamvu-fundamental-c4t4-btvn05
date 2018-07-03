numb = [-10, 0, 5, -20, 2, -100, 2018]


sorted_list = []
sorting = True

while sorting:
    min_numb=min(numb)
    sorted_list.append(min_numb)
    numb.remove(min_numb)

    if len(numb) == 0:
        sorting = False
   
print(*sorted_list)

