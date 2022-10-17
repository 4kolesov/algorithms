Блок по алгоритмам в [Яндекс.Практикуме](https://practicum.yandex.ru/ "Яндекс.Практикуме") длится полтора месяца. Каждый спринт (две недели) дается две задачи, которые проверяются ревьюером. Далее идут шесть решенных мной задач, с описанием задания, его решением и ссылкой на файл .py

------------

###### Спринт 11, задача А. Ближайший ноль
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.
Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.
Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

**Формат ввода**
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.

**Формат вывода**
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.

**[Решение .py](https://github.com/4kolesov/algorithms/blob/main/distance_to_value.py "Решение")**
    
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
    


###### Спринт 11, задача B. Ловкость рук
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4. В нём на каждом раунде появляется конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9.
В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.
Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.

**Формат ввода**
В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра –— по 4 символа в каждой строке. Каждый символ —– либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

**Формат вывода**
Выведите единственное число –— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.

[Решение .py](https://github.com/4kolesov/algorithms/blob/main/score_sleight_of_hand.py "Решение")
    
    def get_score_sleight_of_hand(fingers, matrix, hands=2, numbers='123456789'):
        return sum(
            fingers * hands >= matrix.count(number) > 0 for number in numbers)
    
    
    if __name__ == '__main__':
        print(get_score_sleight_of_hand(
            int(input()), f'{input()}{input()}{input()}{input()}'))
    

###### Спринт 12, задача А. Дек
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.
Внимание: при реализации используйте кольцевой буфер.

**Формат ввода**
В первой строке записано количество команд n — целое число, не превосходящее 100000. Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000. В следующих n строках записана одна из команд:
push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

**Формат вывода**
Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

[Решение .py](https://github.com/4kolesov/algorithms/blob/main/deque.py "Решение .py")
    
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
    

###### Спринт 12, задача B. Калькулятор
**Формат ввода**
В единственной строке дано выражение, записанное в обратной польской нотации. Числа и арифметические операции записаны через пробел.
На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.
Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.

**Формат вывода**
Выведите единственное число — значение выражения.

[Решение .py](https://github.com/4kolesov/algorithms/blob/main/calculator.py "Решение .py")
    
    import operator
    
    
    class Stack:
        def __init__(self):
            self.items = []
    
        def push(self, item):
            self.items.append(item)
    
        def pop(self):
            try:
                return self.items.pop()
            except IndexError:
                raise IndexError('В хранилище отсутствуют элементы')
    
    
    OPERATIONS = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul,
        '/': operator.floordiv
    }
    
    
    def calculator(symbols, stack=None, actions=OPERATIONS, digitizer=int):
        stack = Stack() if stack is None else stack
        for symbol in symbols:
            if symbol in actions:
                operand_1, operand_2 = stack.pop(), stack.pop()
                stack.push(actions[symbol](operand_2, operand_1))
            else:
                try:
                    stack.push(digitizer(symbol))
                except ValueError:
                    raise ValueError(f'Передан некорректный символ: {symbol}')
        return stack.pop()
    
    
    if __name__ == '__main__':
        print(calculator(input().split()))
    

###### Спринт 13, задача A. Поиск в сломанном массиве
Алла ошиблась при копировании из одной структуры данных в другую. Она хранила массив чисел в кольцевом буфере. Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время. Алла скопировала данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности. Теперь массив не является отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за O(log n).
Можно предполагать, что в массиве только уникальные элементы.
Задачу необходимо сдавать с компилятором Make, он выбран по умолчанию, других компиляторов в задаче нет.
Формат ввода
Функция принимает массив натуральных чисел и искомое число 
k
. Длина массива не превосходит 10000. Элементы массива и число k не превосходят по значению 10000.
В первой строке записано число n –— длина массива.
Во второй строке записано положительное число k –— искомый элемент. 
Далее в строку через пробел записано n натуральных чисел – элементы массива.

Формат вывода
Функция должна вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля). Если элемент не найден, функция должна вернуть −1.
Изменять массив нельзя.
Для отсечения неэффективных решений ваша функция будет запускаться от 100000 до 1000000 раз.

[Решение .py](https://github.com/4kolesov/algorithms/blob/main/broken_search.py "Решение .py")
    
    def broken_search(nums, target) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            nums_left = nums[left]
            if nums_left == target:
                return left
            nums_right = nums[right]
            if nums[right] == target:
                return right
            mid = (left + right + 1) // 2
            num_mid = nums[mid]
            if num_mid == target:
                return mid
            if nums_left < num_mid:
                if nums_left < target < num_mid:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if num_mid < target < nums_right:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    

###### Спринт 13, задача B. Эффективная быстрая сортировка
Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров. Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования будет определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов. Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память, то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place").
**Формат ввода**
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:
уникальным логином (строкой из маленьких латинских букв длиной не более 20)
числом решённых задач Pi
штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
**Формат вывода**
Для отсортированного списка участников выведите по порядку их логины по одному в строке.

[Решение .py](https://github.com/4kolesov/algorithms/blob/main/effective_quicksort.py "Решение .py")
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
