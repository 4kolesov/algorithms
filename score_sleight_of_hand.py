# 70599334
def get_score_sleight_of_hand(fingers, matrix, hands=2, numbers='123456789'):
    return sum(
        fingers * hands >= matrix.count(number) > 0 for number in numbers)


if __name__ == '__main__':
    print(get_score_sleight_of_hand(
        int(input()), f'{input()}{input()}{input()}{input()}'))
