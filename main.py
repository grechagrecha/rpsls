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
from utils import CircularDoublyLinkedList, TermColors, CHOISES, do_magic, name_to_number


def main():

    cdll = CircularDoublyLinkedList()

    for elem in CHOISES:
        cdll.append(elem)

    while True:
        print(f'{TermColors.BLUE}Выбери бойца:')
        print(f'''\t\t\t0 - камень
            1 - спок
            2 - бумага
            3 - ящерица
            4 - ножницы
            0 - выход''')

        while True:
            player_choise = str(input()).lower()

            if player_choise in CHOISES.values():
                break
            elif player_choise == '0':
                quit()
            else:
                print(f'{TermColors.RED}Неверный выбор!')

        comp_choise = CHOISES.get(randint(0, 4))
        print(f'{TermColors.BLUE}Выбор компьютера - {comp_choise}!')

        if cdll[name_to_number(player_choise)].next.data == name_to_number(comp_choise) \
                or cdll[name_to_number(player_choise)].next.next.data == name_to_number(comp_choise):
            print(f'{TermColors.RED}Вы проиграли!')
        elif cdll[name_to_number(player_choise)].data == name_to_number(comp_choise):
            print(f'{TermColors.YELLOW}Ничья!')
        else:
            print(f'{TermColors.GREEN}Вы выиграли')

        if int(input(f'{TermColors.BLUE}Введите 1, если хотите сыграть еще.\n')) == 1:
            print(f'{TermColors.BLUE}Штош, сыграем еще!')
            continue
        else:
            break


if __name__ == '__main__':
    main()
