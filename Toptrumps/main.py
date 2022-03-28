# Top Trumps - Pokemon Game
# Jen and Rachel

# MoSCoW Plan
# Must have (Required tasks):
# 1. Generate a random number between 1 and 151 to use as the Pokemon ID number
# 2. Using the Pokemon API get a Pokemon based on its ID number
# 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (★
# https://pokeapi.co/ )
# 4. Get a random Pokemon for the player and another for their opponent
# 5. Ask the user which stat they want to use (id, height or weight)
# 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
#
#
# Should have:
# 1. Points scoring
# 2. Rounds
#
#
# Could have:
# 1. Player input number of rounds
# 2. Stats for each Pokemon from the API
# 3. Game able to determine a winner
#
#
# Won't have:'
# 1. Choice of which pokemon you use
# 2. Use of Harry Potter API



import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


def run():
    print('------------------------')
    print('Welcome to Pokemon! \U0001F3C1')
    print('------------------------')
# Extension -- score tracking and specifying number of rounds
    playerScore = 0
    computerScore = 0
    i = 1

    rounds = int(input("How many rounds do you want to play?: "))

    while i <= rounds:
        my_pokemon = random_pokemon()
        print("")
        print('You were given {}'.format(my_pokemon['name']))
        stat_choice = input('Which stat do you want to use? (id, height, weight) ')
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))
        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]

        if my_stat > opponent_stat:
            print('You Win!')
            playerScore += 1
        elif my_stat < opponent_stat:
            print('You Lose!')
            computerScore += 1
        else:
            print('Draw!')


# Extension -- Added ability to track scores of each player and track no. of rounds
        print("\nScores")
        print(f"Round {i}")
        print(f"You: {playerScore} | Computer: {computerScore}\n")
        print("------------------------")
        print(f"Round {i+1}")
        print("------------------------")
        i += 1


run()

#repeat = input("Play again? (Y or N) ")
#while repeat not in ["Y", "N"]:
    #repeat = input("Invalid choice! Please enter (Y or N): ")

#if repeat == "Y":
    #run()
#else:
    #print('Thanks for playing!')
