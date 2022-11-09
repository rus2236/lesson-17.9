while True:     # проверка соответствия указанному в условии ввода данных последовательности чисел
    numbers = input('Введите числа через пробел: ')
    numbers_without = numbers.replace(' ', '')
    if not numbers_without.isdigit():
        print('ОШИБКА! Введите только числа через пробел!')
    else:
        break

while True:       # проверка соответствия указанному в условии ввода данных единичного числа
    try:
        random_number = int(input('Введите любое число: '))
        break
    except ValueError:
        print("Ошибка! Введите только число!")

list_number = list(map(int, numbers.split()))
print(f'Последовательность чисел в списке: {list_number}')

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы
    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_number = merge_sort(list_number)
print(f'Отсортированный список по возрастанию: {list_number}', )

def binary_search(array, element, left, right):
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находимо середину
        if array[middle] == element:  # если элемент в середине,
           return middle  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине рекурсивно ищем в левой половине
           return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
           return binary_search(array, element, middle + 1, right)
    except IndexError:
        return f'Число {random_number} не входит в диапазон списка'

if not binary_search(list_number, random_number, 0, len(list_number)):
    number_near = min(list_number, key=lambda x: (abs(x - random_number), x))
    ind = list_number.index(number_near)
    max_index = ind + 1
    min_index = ind - 1
    if number_near < random_number:
        print(f'''В списке нет введенного элемента 
Ближайший Больший элемент: {list_number[max_index]}, его индекс: {max_index}
Ближайший Меньший элемент: {number_near}, его индекс: {ind}''')
    elif min_index < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {number_near}, его индекс: {list_number.index(number_near)}
В списке нет меньшего элемента''')
    elif number_near > random_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {number_near}, его индекс: {list_number.index(number_near)}
Ближайший меньший элемент: {list_number[min_index]}, его индекс: {min_index}''')

    elif list_number.index(number_near) == 0:
        print(f'Индекс введенного элемента: {list_number.index(number_near)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_number, random_number, 0, len(list_number))}')


