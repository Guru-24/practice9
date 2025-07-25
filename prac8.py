import random

def welcome():
    print("====================================")
    print("     Welcome to the Guess Game!")
    print(" Try to guess the number (1 to 100)")
    print("====================================")
def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    score = 100
while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            if guess == number:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                print(f"✅ Your score: {score}")
                break
            elif guess < number:
                print("🔼 Too low! Try a higher number.")
            else:
                print("🔽 Too high! Try a lower number.")
            score -= 10
           except ValueError:
            print("❗ Invalid input. Please enter a number.")

    else:
        print(f"\n❌ Game Over! The number was {number}.")
        print(f"Your score: {score}")
def main():
    welcome()
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
if again != 'yes':
            print("Thanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
