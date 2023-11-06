import random


def Decrypt():
    
    #The Decrpyt Does the same steps but in reverse
    #First ask for seed, then format to unicode, subtract seed, then reformat

    seed = int(input('Please input the seed given with the message: '))
    InputString = input('Please input the string: ')

    UnicodeForm = []
    UnicodeForm_after = []
    Output = []

    #This converts the Input to the unicode form 
    for i in InputString:
        x = ord(i)
        UnicodeForm.append(x)
    
    #This removes the seed
    for i in UnicodeForm:
        i = i - seed
        UnicodeForm_after.append(i)

    #This converts back to Ascii
    for i in UnicodeForm_after:
        x = chr(i)
        Output.append(x)


    Final = ''.join(Output)

    print(f'\n\nFinal Outcome: {Final}')
    print(f'Seed: {seed}')


    pass


def Encrypt():
    
    #I want the user to chose if they want to chose the seed or have it randomly generated
    #I will ask the user for the string that is to be encrypted
    #I will output the crypt and the seed

    try:
        seed = int(input('Chose seed (leave blank for random) : '))
    
    #If the int is left empty it will give a ValueError, i decided to catc hit and then make a seed randomiser
    
    except ValueError:
        seed = 1 + random.randint(1, 1100000)
    

    #Now i have a seed i can work on the encryptor
    #This will work by converting each charachter to its Numruacy-Ascii number, then multiplying each number by the seeds random number in order
    #Then converting this number back into Ascii Form

   
    InputString = input("enter the string you wish to be enctrypted\n:")
    UnicodeForm = []
    UnicodeForm_after = []
    Output = []

    #This converts the Input to the unicode form 
    for i in InputString:
        x = ord(i)
        UnicodeForm.append(x)
    
    for i in UnicodeForm:
        i = i + seed
        UnicodeForm_after.append(i)

    for i in UnicodeForm_after:
        x = chr(i)
        Output.append(x)
    
    Final = ''.join(Output)


    print(f'\n\nFinal Outcome: {Final}')
    print(f'Seed: {seed}')

    



    


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