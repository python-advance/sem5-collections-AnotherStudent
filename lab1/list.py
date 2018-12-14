import random

# ---------------------------------------------
# https://habr.com/post/415935/
def insertionSort(data):
	for i in range(len(data)):
		j = i - 1 
		key = data[i]
		while data[j] > key and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
	return data

# ---------------------------------------------
# https://github.com/elluscinia/smoothsort/blob/master/smoothsort.py
import heapq

def numbersLeonardo(size):
    """
    Функция формирует список чисел Леонардо, являющихся размерами куч
    :param size: размер входного массива для плавной сортировки
    :param return: возвращает список чисел Леонардо
    """
    numbers = [1, 1] # начальные элементы для последовательности чисел Леонардо
    nextNumber = numbers[-1] + numbers[-2] + 1
    while len(numbers) >= 2 and size > nextNumber:
        numbers.append(nextNumber)
        nextNumber = numbers[-1] + numbers[-2] + 1
    numbers.reverse()
    return numbers

def doListHeaps(data):
    """
    Функция формирует список куч по числам Леонардо
    :param data: входной массив данных
    :param return: выходной список с кучами
    """
    # формируем список чисел Леонардо для входной последовательности
    leonardoNumbers = numbersLeonardo(len(data))
    # формируем список куч
    listHeaps = [] # финальный список куч
    m = 0 # хвост предыдущей части и начало следующей
    for i in leonardoNumbers:
        if len(data) - m >= i:
            # если оставшаяся нераспределённая часть входного массива данных больше или равна очередному числу Леонардо
            listHeaps.append(data[m : m+i])
            # переходим к оставшейся нераспределённой части
            m += i
    # восстанавливаем свойство кучи для каждой кучи
    for i in listHeaps:
        heapq.heapify(i)
    # так как кучи неубывающие, конечный результат будет заполняться с начала - минимального элемента 
    # до максимального элемента последовательности, то меняем порядок куч на обратный
    listHeaps.reverse()
    return listHeaps

def countIndexes(i, indexes):
    """
    Функция формирует список элементов по заданным индексам
    :param i: индекс, потомки которого ищутся
    :param indexes: список индексов
    :return indexes: список индексов
    """
    indexes.append(2*indexes[i]+1)
    indexes.append(2*indexes[i]+2)

    return indexes

def getList(indexPart, heap):
    """
    Функция формирует подкучу из заданного списка индексов и исходной кучи
    :param indexPart: список индексов 
    :param heap: исходная куча
    :return heapPart: найденная подкуча
    """
    heapPart = []
    for i in indexPart:
        if i < len(heap):
            heapPart.append(heap[i])

    return heapPart

def heapDivision(heap):
    """
    Функция деления кучи на левые и правые подкучи
    :param heap: куча для деления
    :param return: возвращает кортеж из левой и правой подкучи соответсвенно
    """
    heapleft = []
    heapright = []
    index = 0
    indexesLeft = [1] # список индексов для элементов левой подкучи
    indexesRight = [2] # список индексов для элементов правой подкучи
    while indexesLeft[-1] < len(heap): 
        # исходя из логики построения куч, левая подкуча никогда не будет меньше правой

        # считаем индексы для левой подкучи
        indexesLeft = countIndexes(index, indexesLeft)

        # считаем индексы для правой подкучи
        indexesRight = countIndexes(index, indexesRight)

        index += 1

    # составляем списки левой и правой подкуч
    heapleft = getList(indexesLeft, heap)
    heapright = getList(indexesRight, heap)

    return heapleft, heapright

def smoothSort(listHeaps):
    """
    Функция плавной сортировки
    :param listHeaps: кучи
    :param return: отсортированная последовательность данных
    """
    result = []
    while (listHeaps != []):
        # чтобы не писать пустые подкучи
        flag = 0
        # находим минимальный элемент среди корней куч
        min_index = listHeaps.index(min(listHeaps)) # индекс кучи с минимальным корнем
        # меняем его местами с корнем первой кучи
        # запомним корень текущей кучи
        current_root = listHeaps[0][0]
        # и минимальный элемент
        current_min = listHeaps[min_index][0]
        heapq.heapreplace(listHeaps[0], current_min)
        heapq.heapreplace(listHeaps[min_index], current_root)
        # т.к. корень первой кучи будет в дальнейшем удален, размер кучи
        # уменьшится на 1 -> образуются две кучи из его левого и правого поддерева
        if len(listHeaps[0]) > 1:
            heapLeft, heapRight = heapDivision(listHeaps[0])
            flag = 1
        # удаляем корень первой кучи - это минимальный элемент из всех возможных
        minimum = heapq.heappop(listHeaps[0])
        # ставим его в конечную последовательность чисел
        result.append(minimum)
        # удалим первый элемент списка и вставим его ранее полученные поддеревья
        listHeaps.pop(0)
        # добавим две получившиеся кучи в начало всей последовательности куч
        if flag == 1:
            listHeaps.insert(0, heapLeft)
            listHeaps.insert(0, heapRight)
    return result
# ---------------------------------------------

array = [random.randint(0, 99) for _ in range(10)]

print("source: \n", array)
print("insertionSort: \n", insertionSort(array))
print("smoothSort: \n", smoothSort(doListHeaps(array)))
print("sorted: \n", sorted(array))