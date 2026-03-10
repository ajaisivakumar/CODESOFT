import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    comp_score = 0
    
    print("\n--- Rock-Paper-Scissors ---")
    
    while True:
        user_choice = input("\nChoose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        
        if user_choice == 'quit':
            break
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
            
        comp_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")
        
        # Game Logic
        if user_choice == comp_choice:
            print("Result: It's a tie!")
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'scissors' and comp_choice == 'paper') or \
             (user_choice == 'paper' and comp_choice == 'rock'):
            print("Result: You win!")
            user_score += 1
        else:
            print("Result: You lose!")
            comp_score += 1
            
        print(f"Scores -> You: {user_score} | Computer: {comp_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    rock_paper_scissors()