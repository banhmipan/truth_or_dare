# T-O-D (by grandmaster Brendon Tran 😁)
import random

def game():
  truth_rand = random.randint(1, 7)
  dare_rand = random.randint(1, 7)

  truths = [
    'What is something embarrassing that you\'ve done recently?',
    'How many times do you brush your teeth each day?',
    'If you could only spend time with one person during the end of the world, who would it be?',
    'What is something that everyone likes, but you hate?',
    'What is a perfect day to you?',
    'What is your preferred date location?',
    'How do you manage stress?'
  ]

  dares = [
    'Tell your crush that you like them.',
    'Use light theme on everything for an hour.',
    'Shout "BANANA!" at the top of your lungs.',
    'Act drunk for five minutes.',
    'Prank call your best friend and speak in a British accent.',
    'Call both of your parents and tell them that you love them <3',
    'Send an embarrassing image to the first person in your contacts/DMs list.'
  ]

  prompt = int(input('Truth or dare? Select a number.\n1. Truth\n2. Dare\n\n'))
  if prompt == 1:
    if truth_rand == 1:
      print('\n' + truths[1-1])
    elif truth_rand == 2:
      print('\n' + truths[2-1])
    elif truth_rand == 3:
      print('\n' + truths[3-1])
    elif truth_rand == 4:
      print('\n' + truths[4-1])
    elif truth_rand == 5:
      print('\n' + truths[5-1])
    elif truth_rand == 6:
      print('\n' + truths[6-1])
    elif truth_rand == 7:
      print('\n' + truths[7-1])

  if prompt == 2:
    if dare_rand == 1:
      print(dares[1-1])
    elif dare_rand == 2:
      print(dares[2-1])
    elif dare_rand == 3:
      print(dares[3-1])
    elif dare_rand == 4:
      print(dares[4-1])
    elif dare_rand == 5:
      print(dares[5-1])
    elif dare_rand == 6:
      print(dares[6-1])
    elif dare_rand == 7:
      print(dares[7-1])

  elif prompt != 1 and prompt != 2:
    print('Error')

  retry = int(input('\nWould you like to play again? Select a number.\n1. Yes\n2. No\n\n'))
  while retry != 2:
    return game()
  if retry == 2:
    print('\nGoodbye!')

game()