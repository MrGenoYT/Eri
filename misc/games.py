import random

async def rock_paper_scissors(user_choice):
    choices = ['rock', 'paper', 'scissors']
    eri_choice = random.choice(choices)
    if user_choice == eri_choice:
        return f"I chose {eri_choice} too! It's a tie~"
    elif (user_choice == 'rock' and eri_choice == 'scissors') or \
         (user_choice == 'scissors' and eri_choice == 'paper') or \
         (user_choice == 'paper' and eri_choice == 'rock'):
        return f"I picked {eri_choice}... You win this time~!"
    else:
        return f"Ha! I picked {eri_choice}! I win~ 😏"
