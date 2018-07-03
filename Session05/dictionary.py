dic = ["hc" "ng" "pt" "eny" "ns" "ngta" "lm" "r" "stt" ]
print(dic, end="\t")

dic = {
    "hc": "học",
    "ng": "người",
    "pt": "phút",
    "eny": "em người yêu"
}

loop = True
while loop:

    for key in dic.keys():
        print(key, end ="\t")

    print()

    code = input("Your code:")
    if code in dic:
        print("Found")
    else:
        print("Not found")
        contribute = input("Do you want to contribute thí word(Y/N)? ")
        if contribute == "y":
            trans = input("Your translation: ")
            dic[code]= trans
        
        else:
            print("Bye")
            loop = False


