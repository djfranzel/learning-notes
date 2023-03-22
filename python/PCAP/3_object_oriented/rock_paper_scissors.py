
import random

print('--- Rock Paper Scissors Game ---')

choices = ['r', 'p', 's']
rounds_count = 0

class Round():
    def __init__(self, human, computer) -> None:
        self.human = human
        self.computer = computer

    def results(self):
        print('[Game summary] Your points:')

# get a valid value for how many rounds to play
while True:
    rounds_count = input('How many rounds would you like to play? ')
    try:
        rounds_count = int(rounds_count)
        if rounds_count > 0:
            break
    except ValueError:
        continue

# instantiate an empty list for all round objects
all_rounds = []

counter = 0
# keep playing until all rounds have been played
while counter < rounds_count:

    human_choice = input('Rock, paper or scissors [r/p/s]? ')

    # make sure the response is valid! if not, just keep looping
    if not human_choice in choices:
        continue

    counter += 1

    # set the computer choice
    computer_choice = random.choice(choices)

    print('You:', human_choice, '| Computer:', computer_choice)
    if human_choice == computer_choice:
        print('This round is a tie')
        all_rounds.append(Round(0, 0))
    elif human_choice == 'r' and computer_choice == 's' or \
         human_choice == 's' and computer_choice == 'p' or \
         human_choice == 'p' and computer_choice == 'r':
        print('You won this round!')
        all_rounds.append(Round(1, 0))
    else:
        print('You lost this round!')
        all_rounds.append(Round(0, 1))

human_points = 0
computer_points = 0
for round in all_rounds:
    if round.human == 1:
        human_points += 1
    elif round.computer == 1:
        computer_points += 1

# total up all points to determine who won
print('[Game summary] Your points:', human_points, '| Computer points:', computer_points)
if human_points == computer_points:
    print('It was a tie')
elif human_points > computer_points:
    print('You won!')
elif computer_points > human_points:
    print('Computer won!')
else:
    print('Error')