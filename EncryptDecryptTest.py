def encrypt():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open("C:/Users/MONSTER/Desktop/texts/Top secret.txt","r") as source, open("C:/Users/MONSTER/Desktop/texts/minecraft.txt","w") as output:
        for line in source.readlines():
            if "=" in line:
                output.writelines("="*20 + "\n")
            else:
                for char in line:
                    if char.isupper():
                        output.write(uppercase[25-uppercase.index(char)])
                    elif char.islower():
                        output.write(lowercase[25-lowercase.index(char)])
                        pass
                    elif char.isdigit():
                        output.write(str(9-int(char)))
                    else:
                        output.write(char)

def DecryptAndPrint():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open("C:/Users/MONSTER/Desktop/texts/minecraft.txt","r") as source:
        for line in source.readlines():
            for char in line:
                if char.isupper():
                    print(uppercase[25-uppercase.index(char)],end="")
                elif char.islower():
                    print(lowercase[25-lowercase.index(char)],end="")
                    pass
                elif char.isdigit():
                    print(str(9-int(char)),end="")
                else:
                    print(char,end="")
            print("",end="")
        print("")

def EncryptAdd():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open("C:/Users/MONSTER/Desktop/texts/add.txt","r") as source, open("C:/Users/MONSTER/Desktop/texts/minecraft.txt","a") as output:
        output.write("\n")
        output.write("="*20+"\n")
        for line in source.readlines():
            if "=" in line:
                output.writelines("="*20 + "\n")
            else:
                for char in line:
                    if char.isupper():
                        output.write(uppercase[25-uppercase.index(char)])
                    elif char.islower():
                        output.write(lowercase[25-lowercase.index(char)])
                        pass
                    elif char.isdigit():
                        output.write(str(9-int(char)))
                    else:
                        output.write(char)

try:
    encrypt()
except :
    pass
try:
    EncryptAdd()
except :
    pass
DecryptAndPrint()


"""
//
#aga = ("wha", "aga")
#with open("textimsi.txt","r") as file:
#    line = file.read()

#print(line)

#with open("textimsi.txt","r+") as file:

#    #file.write(aga[0])
#    #file.write(aga[0])
#    pass

#with open("textimsi.txt","a") as file:

#file.write("\nbaris,200401020,90,MEG\n")
#pass

#with open("textimsi.txt","r") as file:

#    lines = file.readlines()
#    print(lines)

#with open("textimsi.txt","r") as file:

#    for line in file:
#        row = line.rstrip().split(',')
#        print(f"{row[0]} has {row[2]}")
"""