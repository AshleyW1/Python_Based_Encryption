import random

def Encrypt():
    try:
        seed = int(input('Chose seed (leave blank for random) : '))
    except ValueError:
        seed = 1 + random.randint(1, 1100000)
    
    InputString = input("enter the string you wish to be enctrypted\n:")
    UnicodeForm = []
    UnicodeForm_after = []
    Output = []

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
    pass

def Decrypt():

    seed = int(input('Please input the seed given with the message: '))
    InputString = input('Please input the string: ')

    UnicodeForm = []
    UnicodeForm_after = []
    Output = []

    for i in InputString:
        x = ord(i)
        UnicodeForm.append(x)
    for i in UnicodeForm:
        i = i - seed
        UnicodeForm_after.append(i)
    for i in UnicodeForm_after:
        x = chr(i)
        Output.append(x)

    Final = ''.join(Output)
    print(f'\n\nFinal Outcome: {Final}')
    print(f'Seed: {seed}')
    pass   

def main():
    a = input('1 - Encrypt\n2 - Decrypt\n:')
    if a == "1":
        Encrypt()
    if a == "2":
        Decrypt()
    else:
        main()

main()