
import time
import random
from words import words
import visuals
word = random.choice(words)
#print(list(word))
opt = []
optional = list(word)
for c in range(len(optional)):
    opt.append('-')
#print(f'\n{opt}\n')
#this was used to print word for testing 
#print(word)
c = 1
guesses = []
lives = 8
visuals.dasher(len(optional))

while lives > 1:
    
    #print(f'you have {lives - 2} lives \n')
    if '-' not in opt:
        print('you won')
        break
    guess = input('yo what is ur guess  ')
    
    if guess in optional:
        for r in range(optional.count(guess)):
            opt[optional.index(guess)] = guess
            visuals.update_letter(optional.index(guess), guess)
            
            optional[optional.index(guess)] = '-'
        print(opt)
        visuals.guessinger(1)
    elif guess not in optional:
        lives -= 1
        if lives < 7:
            visuals.visualize(lives)
        visuals.guessinger(0)
    print("your lives left " + str(lives))

visuals.results(lives)
time.sleep(2)  

    
