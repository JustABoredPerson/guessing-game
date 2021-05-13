import random

tries = 0
list_of_words = ["car", "bike", "cat"]
i = random.randint(0,2)
pickedword = list_of_words[i]

print(list_of_words[0], list_of_words[1], list_of_words[2])
guess = input("From the list of words above, guess the word I am thinking of: ")

if guess != pickedword:
    tries += 1
    retry = ''

    while retry != pickedword:

        retry = input("Wrong! Try again: ")
        
        if retry != pickedword:
            tries += 1
            continue
      
        print("Well done! You guessed it in", tries, "tries!")
else:
    print("Well done! You guessed it in", tries, "tries!")
        
    
