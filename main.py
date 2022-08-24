"""

Rock, paper, scissors, lizard, spok game!


Choose your fighter:
    0 - rock
    1 - spok
    2 - paper
    3 - lizard
    4 - scissors

"""


from random import randint
from utils import name_to_number, number_to_name


def main():
    print('Хелло! Поиграем в камень, ножницы, бумага, ящерица, спок?')
    print('Выбери бойца!')
    player_choise = str(input(''))
    print('\n')

    print(f'Хм. Штош, твой выбор - {player_choise.lower()}.\n')
    player_number = name_to_number(player_choise.lower())


if __name__ == '__main__':
    main()
