# 71237216
class Deque:

    def __init__(self, max_size):
        self.elements = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = -1
        self.size = 0

    def push_back(self, value):
        if self.size == self.max_size:
            raise IndexError('Хранилище элементов переполнено')
        self.tail = (self.tail + 1) % self.max_size
        self.elements[self.tail] = value
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            raise IndexError('Хранилище элементов переполнено')
        self.head = (self.head - 1) % self.max_size
        self.elements[self.head] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise IndexError('Хранилище элементов пустое')
        front = self.elements[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return front

    def pop_back(self):
        if self.size == 0:
            raise IndexError('Хранилище элементов пустое')
        back = self.elements[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return back


if __name__ == '__main__':
    quantity_of_commands = int(input())
    deque = Deque(int(input()))
    for _ in range(quantity_of_commands):
        action, *values = input().split()
        try:
            result = getattr(deque, action)(*values)
            if result is not None:
                print(result)
        except IndexError:
            print('error')
        except AttributeError:
            raise AttributeError(f'Некорректный атрибут {action} для {deque}')
