import random


def Decrypt():
    pass


def Encrypt():
    
    #I want the user to chose if they want to chose the seed or have it randomly generated
    #I will ask the user for the string that is to be encrypted
    #I will output the crypt and the seed

    try:
        seed = int(input('Chose seed (leave blank for random)'))
    except ValueError:
        seed = 1 + random.randint(8546, 6854358) 
        seed = seed * random.randint(8546, 6854358)
    
    random.seed(int(seed))
    print(int(seed))
    print(random.randint(0, 10))
    print(random.randint(0, 10))
    print(random.randint(0, 10))


def main():

    #Basic Menu

    a = input('1 - Encrypt\n2 - Decrypt\n:')
    if a == "1":
        Encrypt()
    if a == "2":
        Decrypt()
    else:
        main()

main()