import sys
from src.price_game import price_game

def main():
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == '--non-interactive':
                price_game(non_interactive=True)
            else:
                print("Usage: ./price_game [--non-interactive]")
        else:
            print("Welcome to the Just Right Price game!")
            print("Find the number between 1 and 10000.")
            price_game()
            print("Thank you for playing!")
    except ValueError as ve:
        print(f"Error: {ve}")
        exit(-84)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(84)

if __name__ == "__main__":
    main()