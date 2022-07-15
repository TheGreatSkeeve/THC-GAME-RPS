import random
from datetime import *
import os
clear = lambda: os.system('cls')


class rpsEngine:
    def __init__(self,games):
        self.words = ['rock','paper','scissors']
        self.letters = ['r','p','s']
        self.playerScore = 0
        self.comScore = 0
        self.gameNum = 0
        self.gameEnd = games
        random.seed(datetime.now().microsecond)
        while self.gameNum <= self.gameEnd:
            self.run()

    def getComChoice(self):
        comChoices = [0,0,0]
        for i in range(0,100):
            num = random.randint(0,2)
            comChoices[num] += 1
        final = comChoices.index(max(comChoices))
        print("Computer chose {}".format(self.words[final]))
        return final

    def run(self):
        print("*****************************")
        print("Games Played:  {}\nScore:  {}".format(self.gameNum,self.playerScore))
        print("*****************************\n")
        while True:
            player = str(input("Choose (r)ock, (p)aper, or (s)cissors.\n")).lower()
            if player in self.letters:
                choice = self.letters.index(player)
                print("You chose {}".format(self.words[choice]))
                break

        comChoice = self.getComChoice()

        if choice == comChoice:
            print("\nIt's a tie.")
        elif choice == 0:
            if comChoice == 1:
                print("\nYou lose.")
                self.comScore += 1
            else:
                print("\nYou win!")
                self.playerScore += 1
        elif choice == 1:
            if comChoice == 2:
                print("\nYou lose.")
                self.comScore += 1
            else:
                print("\nYou win!")
                self.playerScore += 1
        self.gameNum += 1
        input("Press enter to continue.")
        clear()

gameCount = int(input("How many games do you want to play?"))
rpsEngine(gameCount)
