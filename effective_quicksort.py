# 72009441
def effective_quicksort(rivals):
    def partition(left, right):
        pivot = rivals[left]
        left_index, right_index = left + 1, right - 1
        while True:
            if left_index <= right_index and pivot < rivals[right_index]:
                right_index -= 1
            elif left_index <= right_index and rivals[left_index] < pivot:
                left_index += 1
            elif rivals[left_index] < pivot < rivals[right_index]:
                continue
            if left_index <= right_index:
                rivals[left_index], rivals[
                    right_index] = rivals[right_index], rivals[left_index]
            else:
                rivals[left], rivals[
                    right_index] = rivals[right_index], rivals[left]
                return right_index

    def quicksort(left, right):
        if (right - left) > 1:
            section = partition(left, right)
            quicksort(left, section)
            quicksort(section + 1, right)

    quicksort(0, len(rivals))
    return rivals


if __name__ == '__main__':
    print(*[name for _, _, name in effective_quicksort([
        (lambda login, done, penalty: (-int(done), int(penalty), login))(
            *(input().split())) for _ in range(int(input()))])
    ], sep='\n')
