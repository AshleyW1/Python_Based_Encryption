# Python_Based_Encryption
Python Encryption Program (Named 'PeP')


### Encryption Method
```py
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
```

### Seed Gathering
```py
def Encrypt():
    try:
        seed = int(input('Chose seed (leave blank for random) : '))
    except ValueError:
        seed = 1 + random.randint(1, 1100000)
    ...
```
I have given the user to either chose their own seed or let a random one be chosen.
due to unicode having 1,114,111 bits, i though it would be best to cap the random.randint function to 1,100,000, so it can never go over, when used correctly

### Encryption
```py
    ...
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
    ...
```
At the start i thought it would be a good idea to creat the lists i would be needing in the future, then underneith, the first iteration converts the string to the unicode form, the second alters the unicode number with help from the seed, then the final step is to convet the unicode number back into ascii.
```py
    ...
    Final = ''.join(Output)
    print(f'\n\nFinal Outcome: {Final}') 
    pass
```
This was then followed with the method used to form the final string, i decided to join the list in 'Output' by nothing, i did this because spaces are also acii characters, so there is no need to seperate the characters manually.

### Decryption Method

```py
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
    ...
```
This method is the exact same as the method used to encrypt the message, the only differeces are, here we ask the user what the seed is, to see if they have permission to decrypt the message, also during the stage where the seed manipulates the unicode, we take away the seed rather than add it.
```
    ...
    Final = ''.join(Output)
    print(f'\n\nFinal Outcome: {Final}')
    print(f'Seed: {seed}')
    pass  
```
This is the same finishing method used in the Encryption method.

# Issues with this code

My main issue with this program is how easy it is to crack it, the method i would use is, get the string, and subtract each part of it until a lot of the repeating characters all transform into spaces, at this point i would run a dicitonary check on some of the words to prove that it is correct, the nthat would be the correct outcome from the encrypted message.

This code is very rudimentary and should be seen as a proof of concept rather than an actual product.

Discord: @ashley.txt