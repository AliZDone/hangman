#documentation part
animals_name = ['cat',"dog","monkey","zebra"]
objects_name = ['sofa','table','chair',"television"]
cars_name = ['ford','bmw',"volvo","benz"]

#code:
import time
import os
import random as rand
import re

class hangman:
    def __init__(self):
        hangman.get()

    def choose(name):
        random = rand.randint(0,len(name)-1)
        return name[random]

    def get():
        while True:
            category = input('enter witch category want to play "animal", "cars", "objects" please enter the categorys correctly: ')
            if category == 'animal':
                animal = hangman.choose(animals_name)
                hangman.play(animal)
            elif category == 'cars':
                car = hangman.choose(cars_name)
                hangman.play(car)
            elif category == "objects":
                Object = hangman.choose(objects_name)
                hangman.play(Object)
            else:
                print("wrong category!")
                time.sleep(2)
                os.system('cls')
                continue

    def len_placement(name):
        len_name = len(name)
        s = ""
        for i in range(len_name):
            s += " _"
        return s
    
    def placement(name, guess, filed):
        filed = list(filed)
        for index,char in enumerate(name,start=1):
            if char == guess:
                filed[(index*2)-1] = guess
        filed = "".join(filed)
        test = re.findall('[_]',filed)
        if test == []:
            return filed, True
        else:
            return filed, False

                
    def play(name):
        name = re.findall(r'[a-zA-Z]',name)
        name1 = set(name)
        filed = hangman.len_placement(name)
        health = 9
        win_flag = False
        win = False
        while health > 0 :
            print("health :",health)
            print("\n")
            print(filed)
            guess = input("Enter you guess: ")
            if guess in name1:
                filed, win = hangman.placement(name,guess,filed)
                if win == True:
                    win_flag = True
                    break
            else:
                health -= 1
                print("The answer you choose was incorrect please try anoter one!")
                time.sleep(2)
            os.system("cls")
            
        if win_flag == True:
            os.system("cls")
            print(filed)
            print("you win!")
            print("Good job")
        else:
            print("you lose!")
        
        time.sleep(2)
        os.system("cls")
        ans = input("Do want to play again?(Y/N) ")
        ans = ans.lower()
        if ans == 'y':
            hangman.__init__(self=1)
        else:
            exit()
#end of class hangman

#main:
hangman()

