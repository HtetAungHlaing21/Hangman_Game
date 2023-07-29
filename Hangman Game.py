# Hangman Game
import random

myWords=open("Words.txt", "r")

temp=myWords.read()
wordList=temp.split(",")

myWords.close()

def show_chances(chances):
    if chances==5:
        return "\n O\n"
    elif chances==4:
        return "\n O\n |"
    elif chances==3:
        return "\n O\n/|"
    elif chances==2:
        return "\n O\n/|\\"
    elif chances==1:
        return "\n O\n/|\\\n/"
    elif chances==0:
        return "\n O\n/|\\\n/ \\"

secretWord=random.choice(wordList).lower()  #to make sure every letter is in lowercase
length=len(secretWord)
chances=6
guessList=[]
print("Welcome to Hangman Game!")
print("_ "*length)
print("You have 6 chances.\n")
while chances>0:
    wordLeft=0
    guess=input("Guess a letter. Your guess: ")
    if guess.isalpha() & len(guess)==1:    #The input must be only one letter
        if guess in guessList:             #The repeated letters will not be tested.
            print("This letter is already guessed. Try another letter.")
        else:
            guess=guess.lower()                #change it into lowercase if it is upper
            guessList.append(guess)
            for item in secretWord:
                if item in guessList:
                    print(item, end=" ")
                else:
                    print("_", end=" ")
                    wordLeft+=1
            if guess in secretWord:
                print("\nYou are correct!")
            else:
                chances-=1
                print("\nSorry! Wrong Guess")
                print(show_chances(chances))
            if chances==0:
                print("\nGame Over! You lost!")
                print("The secret word is '"+ secretWord + "'")
            if wordLeft==0:
                print("Congratulations! You won!!")
                break
    else:
        print("Invalid Input! Please Try again!")
print("\nThanks for playing Hangman Game!")