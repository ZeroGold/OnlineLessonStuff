from random import randint

### NEED AN ANIMATOR FOR EACH PORTION

def game1():
    game = True


    while game:
        this = input()
        i = randint(1,100)
        try:    
            if int(this) ==  i:
                print("Condition 1")
                game2()
            if int(this) % 2 == 0:
                if i % 2 == 0:
                    print("You Won")
                    game =  False
            if int(this) % 2 == 1:
                if i % 2 == 1:
                    print("You Won")
                    game = False
        except:
            print("Please type an integer")



def shuffle(arr):
    # Start from the last element and swap one by one. We don't
    # need to run for the first element that's why i > 0
    n = len(arr)
    for i in range(n-1):
        # Pick a random index from 0 to i
        j = randint(0,i+1)
 
        # Swap arr[i] with the element at random index
        arr[i],arr[j] = arr[j],arr[i]
    return arr


def game2():
## HOW TO MAKE SHUFFLE GAME HARDER?
## IF THEY GET IT WRONG? IT SHUFFLES AGAIN WITHOUT TELLING THEM SO IT'S FULLY POSSIBLE THAT THE SECOND TIME THE CORRECT ANSWER COULD BE THE PREVIOUS SELECTION.
## MULTIPLE ROUNDS??? <-- THIS VIOLATES THE TIME COMPLEXITY RULE BUT MAY BE THE ONLY DETERMINER OF EXTRA DIFFICULTY WHEN SHUFFLING
    a = [1,0,0,0]
### Shuffle 1s in the array and reward for finding the one
    negative = 1
    a = shuffle(a)
    while negative != 0:
        print("Pick 1, 2, 3, 4")
        a = shuffle(a)
        this = input()
        try:
            
            if a[int(this)-1] == 1:
                print("You picked the right one")
                if negative > 2:
                    if negative % 2 == 0:
                        negative/=2
                    if negative-4 > 10:
                        negative -= 10
                    if negative % 2 == 1:
                        negative =(negative+1)/2
                else:
                    negative-=1
            else:
                negative+=1
                print(negative)
                print("Try again")
        except:
            print("Please make a selection")
    
### I.E [0,0,0,1]  -> [0,1,0,0]  picking the second slot wins
    #print("Shuffling")
    #print(a)
    
### FISHER YATES ALGO TO SHUFFLE
### Then match and new condition.




    #game3()




### AT THE END OF THE GAME THEY WIN AN NFT?


    ### only 10 availible

### IN THE MIDDLE THEY RANDOMLY PLAY AN RPG, BUT IT'S HARD

### MAKE IT DIFFICULT?


    ### RPG IS VERY SHORT, BUT THEY FIGHT MAYBE 10 MONSTERS AND A BOSS AS A DETERRENT
    ### PUT HASHES AFTER EVERY MONSTER THAT THEY NEED TO COLLECT AND COMBINE TO UNLOCK GAME 4

    

    ## ON RPG SPAWN  they get a full team and items, but the monster A.I is strong.
### DONT MAKE HARD BECAUSE OF TIME COMPLEXITY, MAKE HARD WITH SKILL.

### NFTS grant acccess to UNDERWORLD




#### MAKE IT FREE BY GIVING 50 DOLLARS OF SOL, so they can pay the gas fee to recieve the NFT and mint from the last game.

### THESE 10 NFTS ARE ONLY GIVING EARLY ACCESS SO THEY GET A HEAD START AT GAME 4
### THEY SHOULD GET OTHER PERKS TOO



game2()
