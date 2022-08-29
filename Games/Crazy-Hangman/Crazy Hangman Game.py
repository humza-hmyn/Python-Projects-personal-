
extra_mode=0
aggro = 1
user_valid = 1
user_name = input("What is your name? ")
while user_valid == 1:
    usr_chc=input("Hello, "+user_name+". Wanna play a game! (Y/N)")
    if usr_chc == ('Y' or 'y'):
        user_valid = 0
    elif usr_chc == ("N" or "n"):
        print("Wow, what a WUSS! Bye.")
        quit()
    elif usr_chc == "harder":
        print("ULTRA NIGHTMARE UNLOCKED\n")
        extra_mode=1
    elif usr_chc == "poop":
        print("very funny - caca mode engaged . . .")
        extra_mode=2
    else:
        if aggro<=3:
            print("Oops! That's an invalid input, try again!\n")
            aggro += 1
        elif aggro==4:
            print("You have literally 2 choices to select from. Try again.\n")
            aggro += 1
        elif aggro==5:
            print("YOU IDIOT CHOOSE BETWEEN 'Y' OR 'N' ITS NOT THAT HARD TRY AGAIN!\n")
            aggro += 1
        elif aggro>5:
            print("\nYou're messing with me, aren't you... please NEVER COME BACK")
            quit()
#init the actual hangman game
print("We'll be playing hangman today\n")
if aggro >= 3:
    print("Let's please pay close attention to the rules, okay?\n")
print("Select your difficulty:\t(Enter respective number for each difficulty)")
if aggro>3:
    print("hopefully this is easier to understand...")
print("EASY: 1"
      "\t MEDIUM: 2"
      "\t HARD: 3"
      "\t NIGHTMARE: 4")
if extra_mode==1:
    print("ULTRA NIGHTMARE: 4 (VERY LONG WORD + 1 MINUTE TIMER)")
elif extra_mode==2:
    print("CACA MODE HAS BEEN SELECTED - HAVE FUN YOU IMMATURE SCHMUCK")
    #print a poop emoji everytime the user enters a letter. They cant win or lose. "Quit" escapes the game.

