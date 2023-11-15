import random 

def Generator(wordsArray,specialCharArray):
    print(wordsArray)

    randomNumber1 = random.randint(1,len(wordsArray)-1)
    randomNumber2 = random.randint(1,len(wordsArray)-1)
    randomNumber3 = random.randint(1,len(specialCharArray)-1)
    password= (wordsArray[randomNumber1]+specialCharArray[randomNumber3] + wordsArray[randomNumber2]).capitalize()
    print(password)
    return password
    

