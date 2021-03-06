import random

tries = 0
y = 0

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def inputtingwords(numwords):
    i = 2
    list_of_words = []
    words = input("Please input " + str(numwords) + " words to guess from: ")
    list_of_words.append(words)
    while i <= numwords:
        if i == 2:
            words = input("2nd word: ")
            list_of_words.append(words)
        elif i == 3:
            words = input("3rd word: ")
            list_of_words.append(words)
        elif i == 4:
            words = input("4th word: ")
            list_of_words.append(words)   
        elif i == 5:
            words = input("5th word: ")
            list_of_words.append(words) 
        elif i == 6:
            words = input("6th word: ")
            list_of_words.append(words)
        elif i == 7:
            words = input("7th word: ")
            list_of_words.append(words)
        elif i == 8:
            words = input("8th word: ")
            list_of_words.append(words)
        elif i == 9:
            words = input("9th word: ")
            list_of_words.append(words)
        elif i == 10:
            words = input("10th word: ")
            list_of_words.append(words)
        i+=1
        continue
    return list_of_words

def easy():

    global y
    global tries
    list_of_words = inputtingwords(3)

    print("Your list of words are: --->",list_of_words[0],",",list_of_words[1],",",list_of_words[2],"<---\n""\nThe computer has picked a word, guess which word the computer picked: ")
    pickedword = random.choice(list_of_words)

    guess = input("Your guess: ")

    if guess != pickedword:
        tries += 1
        retry = guess

        while retry != pickedword:

            while True:
                if list_of_words[y] == retry:
                    list_of_words[y] = strike(list_of_words[y])
                    print("\nYour list of words are: --->",list_of_words[0],",",list_of_words[1],",",list_of_words[2],"<---\n")
                    y = 0
                    break
                else:
                    y+=1
                if y >= len(list_of_words):
                    break
                    

            retry = input("Wrong! Try again: ")
            
            if retry != pickedword:
                y = 0
                tries += 1
                continue
        
            print("Well done! You guessed it in", tries, "tries! The word was " + pickedword)
    else:
        print("Well done! You guessed it first try! The word was " + pickedword)
        
def normal():

    global y
    global tries
    list_of_words = inputtingwords(5)

    print("Your list of words are: --->",list_of_words[0],",",list_of_words[1],",",list_of_words[2],",",list_of_words[3],",",list_of_words[4],"<---\n""\nThe computer has picked a word, guess which word the computer picked: ")
    pickedword = random.choice(list_of_words)

    guess = input("Your guess: ")

    if guess != pickedword:
        tries += 1
        retry = guess

        while retry != pickedword:

            while True:
                if list_of_words[y] == retry:
                    list_of_words[y] = strike(list_of_words[y])
                    print("\nYour list of words are: --->",list_of_words[0],",",list_of_words[1],",",list_of_words[2],",",list_of_words[3],",",list_of_words[4],"<---\n")
                    y = 0
                    break
                else:
                    y+=1
                if y >= len(list_of_words):
                    break
                    

            retry = input("Wrong! Try again: ")
            
            if retry != pickedword:
                y = 0
                tries += 1
                continue
        
            print("Well done! You guessed it in", tries, "tries! The word was " + pickedword)
    else:
        print("Well done! You guessed it first try! The word was " + pickedword)

def hard():

    global y
    global tries
    list_of_words = inputtingwords(10)

    print("\nYour list of words are: --->",list_of_words[0],",",list_of_words[1],",",list_of_words[2],",",list_of_words[3],",",list_of_words[4],",",list_of_words[5],",",list_of_words[6],",",list_of_words[7],",",list_of_words[8],",",list_of_words[9],"<---\n""The computer has picked a word, guess which word the computer picked: ")
    pickedword = random.choice(list_of_words)

    guess = input("Your guess: ")

    if guess != pickedword:
        tries += 1
        retry = guess

        while retry != pickedword:

            while True:
                if list_of_words[y] == retry:
                    list_of_words[y] = strike(list_of_words[y])
                    print("\nYour list of words are: --->",list_of_words[0],",",list_of_words[1],",",list_of_words[2],",",list_of_words[3],",",list_of_words[4],",",list_of_words[5],",",list_of_words[6],",",list_of_words[7],",",list_of_words[8],",",list_of_words[9],"<---")
                    y = 0
                    break
                else:
                    y+=1
                if y >= len(list_of_words):
                    break
                    

            retry = input("Wrong! Try again: ")
            
            if retry != pickedword:
                y = 0
                tries += 1
                continue
        
            print("Well done! You guessed it in", tries, "tries! The word was " + pickedword)
    else:
        print("Well done! You guessed it first try! The word was " + pickedword)

print("................................")
print("\tGuessing Game")
print("................................")

print("Welcome to the guessing game where you have to guess a word the computer picked from your choice of words!")
difficulty = str(input("Would you like to play in 'easy', 'normal' or 'hard' mode?\nIf you want more information, input 'help': "))

if difficulty == 'help':
    print("Easy - You guess from your choice of 3 words.\nNormal - You guess from your choice of 5 words.")
elif difficulty == 'easy':
    easy()
elif difficulty == 'normal':
    normal()
elif difficulty == 'hard':
    hard()