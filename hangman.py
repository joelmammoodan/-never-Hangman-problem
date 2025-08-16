import time
import random
#the word to be guessed
words=['camel','bookshelf','balcony','keyboard','window','minimmum','paper']
a=random.choice(words)


#list of all letters
chars=list('aeioubcdfghjklmnpqrstvwxyz')
display='-'*len(a)
#used to check the letter and then remove it
splt=list(a)
#will store the path it travels
path=[]

visited=set()

#checks whether the letter is correct and removes from splt and updates display
def check(splt,letter):
    global display
    if(letter in splt):
        for k in range(len(a)):
            if(a[k]==letter):
                display=display[:k]+letter+display[k+1:]
        splt.remove(letter)

        return True
    else:

        return False

#to draw the hangmans
def draw(guess):
    if(guess==5):
        print('''\t\t_____________
                  |      |
                  |     |_|
                  |
                  |
                  |
                  |
                --+-----------''')
    elif(guess==4):
        print('''\t\t_____________
                  |      |
                  |     |_|
                  |      |
                  |      |
                  |
                  |
                --+-----------''')
    elif(guess==3):
        print('''\t\t_____________
                  |      |
                  |     |_|
                  |      |
                  |      |
                  |     /
                  |
                --+-----------''')

    elif(guess==2):
        print('''\t\t_____________
                  |      |
                  |     |_|
                  |      |
                  |      |
                  |     / \\
                  |
                --+-----------''')
    elif(guess==1):
        print('''\t\t_____________
                  |      |
                  |     |_|
                  |      |
                  |     /|
                  |     / \\
                  |
                --+-----------''')
    elif(guess==0):
        print('''\t\t_____________
                  |      |
                  |     |_|
                  |      |
                  |     /|\\
                  |     / \\
                  |
                --+-----------''')
    else:
        print('''\t\t_____________
                  |      |
                  |
                  |
                  |
                  |
                  |
                --+-----------''')

def hang(letter,guess):
    #Base Conditions
    #if the final answer is correct
    if(a==display):
        return True
    #if guess finishes go back to the previous recusion and pop the wrong element
    if(guess<=0):
        path.pop()
        return False

    #add the letter to the visited so that it wont check again
    visited.add(letter)


    #repeat hang on every letter and check if it right,if yes:then go for next recursion,if no reduce the guess
    for i in chars:
        #no need to check the same word again
        if(i in visited):
            continue
        #add the letter to path
        path.append(i)
        if(check(splt,i)):
            if(hang(i,guess)):
                return True
        else:
            if(hang(i,guess-1)):
                return True

    return False




def hangman1(tim):
    hang('-',5)
    guess=5
    splt=set(list(a))
    dis='-'*len(a)
    for i in path:
        print("Enter your guess:",end='')
        print(i)
        time.sleep(tim)
        time.sleep(tim)
        if(check(splt,i)):
            print("\t\tCORRECT GUESS\t\t")
            for k in range(len(a)):
                if(a[k]==i):
                    dis=dis[:k]+i+dis[k+1:]
            print('\t\t    ',dis)
        else:
            print(f"\t\tWRONG GUESS......({guess}Guesses left)")
            draw(guess)
            guess-=1
            print('\t\t    ',dis)
        if(a==dis):
            print("You have guess the word correctly")
            break


hangman1(1)
