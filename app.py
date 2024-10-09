from colorama import Style, init, Back
import random as rd
from time import sleep
import os

init(autoreset=True)

# Colors
DEFAULT = '\033[0m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
YELLOW = '\033[3m\033[1;33m'
YELLOW2 = '\033[1;93m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
BOLD = '\033[1m'
BLINK = '\033[5m'

# Styles
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORMAL = Style.NORMAL
RESET_ALL = Style.RESET_ALL

# Background Colors
BACK_BLACK = Back.BLACK
BACK_RED = Back.RED
BACK_GREEN = Back.GREEN
BACK_YELLOW = Back.YELLOW
BACK_BLUE = Back.BLUE
BACK_MAGENTA = Back.MAGENTA
BACK_CYAN = Back.CYAN
BACK_WHITE = Back.WHITE

def print_title():
    print("""
    {3}██████╗ ██╗   ██╗███████╗███████╗███████╗     ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ {0}
    {3}██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗{0}
    {3}██║  ███╗██║   ██║█████╗  ███████╗███████╗    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝{0}
    {3}██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗{0}
    {3}╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║{0}
    {3}╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝{0}
                                                                                                    {6}~{3} Gabriel Machado
                        {2}_______________________________________{0}
                        {2}/                                       \{0}
                        {2}\   {2}I wrote the fastest guess number!{2}   /{0}.
              {3}.    ___{0}   {2}\____   ______________________________/{0}
                  {3}/   ＼{0}      {2}\ノ{0}
                {3}∠)_ ● /  {5}/\ /\{0}                         {6}~{3} GitHub: {1}https://github.com/gabriel-machado-dev
                   {3}/ /__{5}( • ω •){3}__{0}                     {6}~{3} Insta: {1}https://www.instagram.com/_assismachado_/
                  {3}(       {5}∪ ∪{3}     ){0}
                {6}~~~~~~~~~~~~~~~~~~~~~~~~~{0}

    """.format(DEFAULT, GREEN, RED, YELLOW, BLINK, MAGENTA, BLUE))

def instructions():
    print(f"{YELLOW}{BACK_MAGENTA}Instructions:{DEFAULT}")
    print(f"{YELLOW}1. {DEFAULT}{CYAN}You have to guess a number between 🥇 and 💯.{DEFAULT}")
    print(f"{YELLOW}3. {DEFAULT}{CYAN}The game will give you {BACK_MAGENTA}hints{RESET_ALL} {CYAN}to help you guess the number.{DEFAULT}")
    print(f"{YELLOW}4. {DEFAULT}{CYAN}{DIM}Good luck! 👾{DEFAULT}")
    print(f"{YELLOW}5. {DEFAULT}{CYAN}To exit the game, type {RED}'exit'{DEFAULT}")

def guess_number():
    number = rd.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess =input(f"{YELLOW}Guess a number between 1 and 100: {DEFAULT}")
            if guess.isdigit() == False or int(guess) < 1 or int(guess) > 100:
                raise ValueError

            guess = int(guess)
    
            print('')
            if guess == number:
                print('')
                print(f"{GREEN}Congratulations! You guessed the number in {attempts} attempts! 🎉{DEFAULT}")
                break
            elif guess < number:
                print(f"{RED}The number is higher!{DEFAULT}")
                print('')
            elif guess > number:
                print(f"{RED}The number is lower!{DEFAULT}")
                print('')
            attempts += 1
        except ValueError:
            if guess == "exit":
                print('')
                print(f"{YELLOW}Exiting the game...{DEFAULT}")
                print(f'{YELLOW}Come back soon! 🚀{DEFAULT}')
                sleep(2)
                break
            print('')
            print(f"{RED}Please, type a valid number!{DEFAULT}")
            print(f'{RED}The number must be between 1 and 100!{DEFAULT}')
            print(f'{BACK_MAGENTA}{YELLOW}This program only accepts numbers!{DEFAULT}')
            print('')

def main():
    os.system("clear") if os.name == "posix" else os.system("cls")
    print_title()
    instructions()
    print('')
    guess_number()

if __name__ == "__main__":
    main()
    while True:
        play_again = input(f"{YELLOW}Do you want to play again? (yes/no): {DEFAULT}")
        if play_again.lower() == "yes":
            main()
        elif play_again.lower() == "no":
            print('')
            print(f"{YELLOW}Exiting the game...{DEFAULT}")
            print(f'{YELLOW}Come back soon! 🚀{DEFAULT}')
            sleep(2)
            break
        else:
            print('')
            print(f"{RED}Please, type a valid answer!{DEFAULT}")
            print(f'{RED}Type "yes" to play again or "no" to exit the game.{DEFAULT}')
            print('')
