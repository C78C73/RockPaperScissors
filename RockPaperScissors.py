import random

def main():

    userLives = 3
    cpuLives = 3

    choices = ['rock', 'paper', 'scissors']

    while True:
        
        #user picks the choice
        userChoice = str(input("\nChoose: Rock, Paper, or Scissors: ")).lower()

        #CPU randomly gets a choice
        cpuChoice = random.choice(choices)

        #rock
        if (userChoice == "rock" and cpuChoice == "paper"):
            print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
            userLives -= 1
            print(f"\nUser lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
        elif (userChoice == "rock" and cpuChoice == "scissors"):
            print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
            cpuLives -= 1
            print(f"\nCPU lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")

        #paper
        elif (userChoice == "paper" and cpuChoice == "scissors"):
            print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
            userLives -= 1
            print(f"\nUser lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
        elif (userChoice == "paper" and cpuChoice == "rock"):
            print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
            cpuLives -= 1
            print(f"\nCPU lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
            
        #scissors
        elif (userChoice == "scissors" and cpuChoice == "rock"):
            print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
            userLives -= 1
            print(f"\nUser lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")          
        elif (userChoice == "scissors" and cpuChoice == "paper"):
            print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
            cpuLives -= 1
            print(f"\nCPU lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
        else:
            print(f"\nTIE\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
            print(f"\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
            

        if (cpuLives == 0):
            print("User WINS\n")
            break 
        elif (userLives == 0):
            print("\nCPU WINS\n")
            break

main()