import random

def main():

    userLives = 3
    cpuLives = 3

    choices = ['rock', 'paper', 'scissors']

    while True:
        
        try:
            #user picks the choice
            userChoice = str(input("\n-----------------------------------------\nChoose: Rock, Paper, or Scissors: ")).lower()
        except Exception as Error:
            print(f"Error: {Error}")
            continue
        
        print("-----------------------------------------")

        #CPU randomly gets a choice
        cpuChoice = random.choice(choices)

        #rock
        if (userChoice == "rock" and cpuChoice == "paper"):
            userLives, cpuLives = UserLost(userChoice, cpuChoice, userLives, cpuLives)  
        elif (userChoice == "rock" and cpuChoice == "scissors"):
            userLives, cpuLives = CPULost(userChoice, cpuChoice, userLives, cpuLives)

        #paper
        elif (userChoice == "paper" and cpuChoice == "scissors"):
            userLives, cpuLives = UserLost(userChoice, cpuChoice, userLives, cpuLives)  
        elif (userChoice == "paper" and cpuChoice == "rock"):
            userLives, cpuLives = CPULost(userChoice, cpuChoice, userLives, cpuLives)
            
        #scissors
        elif (userChoice == "scissors" and cpuChoice == "rock"):
            userLives, cpuLives = UserLost(userChoice, cpuChoice, userLives, cpuLives)         
        elif (userChoice == "scissors" and cpuChoice == "paper"):
            userLives, cpuLives = CPULost(userChoice, cpuChoice, userLives, cpuLives)
        else:
            userLives, cpuLives = Tie(userChoice, cpuChoice, userLives, cpuLives)
            
        # end game
        if (cpuLives == 0):
            print("User WINS\n")
            break 
        elif (userLives == 0):
            print("\nCPU WINS\n")
            break

def UserLost(userChoice, cpuChoice, userLives, cpuLives):
    print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
    userLives -= 1
    print(f"\nUser lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
    return userLives, cpuLives

def CPULost(userChoice, cpuChoice, userLives, cpuLives):
    print(f"\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
    cpuLives -= 1
    print(f"\nCPU lost a life\n\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
    return userLives, cpuLives

def Tie(userChoice, cpuChoice, userLives, cpuLives):
    print(f"\nTIE\nUser picked: {userChoice} \nCPU picked: {cpuChoice}")
    print(f"\nCPU lives: {cpuLives} left\nUser lives: {userLives} left")
    return userLives, cpuLives

main()