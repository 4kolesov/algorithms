# 70744097
def get_min_distances_to_zero(houses, value='0'):
    zeros = [pos for pos, element in enumerate(houses) if element == value]
    number_of_houses = len(houses)
    result = [0] * number_of_houses
    first, last = zeros[0], zeros[-1]
    result[:first] = [first - pos for pos in range(first)]
    for left, right in zip(zeros, zeros[1:]):
        result[left + 1:right] = [
            min(pos - left, right - pos) for pos in range(left + 1, right)]
    result[last + 1:] = [
        pos - last for pos in range(last + 1, number_of_houses)]
    return result


if __name__ == '__main__':
    input()
    print(*get_min_distances_to_zero(input().split()))
