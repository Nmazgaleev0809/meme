import random

first = ['F','G','E','k']
second = [1,2,3,4,5]
third=['A','B','C','D','E']
zods=[
      'owen',
      'else'
      ]

def get_predictions():
    return f'{random.choice(first)} {random.choice(second)} {random.choice(third)}'

