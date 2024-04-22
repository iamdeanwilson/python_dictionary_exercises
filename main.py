'''
# Write your return_cost function here:
def return_cost(menu, item):
  if item in menu:
    return menu[item]
  return 0

# Write your fanciest_flavor function here:

def fanciest_flavor(menu):
  max_value = 0
  max_key = ""
  for key, value in menu.items():
    if value > max_value:
      max_value = value
      max_key = key
  return max_key

def main():
  flavors = {
    'chocolate' : 0.35,
    'vanilla' : 0.35,
    'strawberry' : 0.42,
    'cookies and cream' : 0.45,
    'mint chocolate chip' : 0.42,
    'fudge chunk' : 0.45,
    'saffron' : 2.25,
    'garlic' : 0.05
  }

  choice = 'strawberry'
  price = return_cost(flavors, choice)
  if price == 0:
    print("Sorry, we don't have {0}.".format(choice))
  else:
    print(f"The price for {choice} is ${price} per scoop.")

# Uncomment the lines below after you code your fanciest_flavor function.
  print('---')
  expensive_flavor = fanciest_flavor(flavors)
  print(f"The most expensive flavor we have is {expensive_flavor}.")

main()

#!/bin/python3
import random

# Code your assign_tickets function here:

def assign_tickets(list):
  ticket_holders = {}
  for name in list:
    ticket_holders[name] = random.randint(100, 500)

  return ticket_holders

# Code the fix_tickets function here:

def fix_tickets(list):
  for (key, value) in list.items():
    if 100 <= value <= 199:
      list[key] += 500


def main():
  names = ['Caleb', 'Naomi', 'Owen', 'Ava', 'Aaron', 'Lydia']
  ticket_holders = assign_tickets(names)
  print(ticket_holders)
  fix_tickets(ticket_holders)
  print(ticket_holders)

if __name__ == '__main__':
  main()

'''

#!/bin/python3
import string

lowercase_letters = string.ascii_lowercase

# Code your character_count function here:

def character_count(string):
  counts = {}
  for char in string.lower():
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1

  return counts


def main():
  text = "B-A-L-L-O-O-N-S!"
  results = character_count(text)
  results_list=list(results.keys())
  results_list.sort()
  print(f"The character counts for '{text}' are:")
  for index in results_list:
    if index in lowercase_letters:
      print(f"{index}: {results[index]}")

if __name__ == '__main__':
  main()