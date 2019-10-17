
"""
# IT WAS THE SECOND TRY/////////////////////////////////////////////////////////
def abc(text):
#создаем функцию перебора букв в тексте
    all=1

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z','(',')','.',',','=','+','-','*','/',
    ':','_','#','[',']','1','2','3','4','5','6','7','8','9','0','<','>','а','б',
    'в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у',
    'ф','х','ц','ш','щ','ч','ъ','ь','э','ы','ю','я', '!', '"', "'",'\\',';','%',
    '&']

    # список всех букв для перебора
    nums = []
    num_for_poryadok = 0
    for letter in letters:
          num = 0
          #считает частоту встречаемости каждой буквы и записываетв  список
          num += 1
          letter_num = text.count(letter)
          nums.append(letter_num)
    for perebor in range(10):
         #считает колво 5 самых часто встречаемых букв
        chislo = max(nums)
        if all<sum(nums):
            all = sum(nums)
        letter_index = nums.index(chislo)
        num_for_poryadok+=1
        nums[nums.index(chislo)] =1
        print(str(num_for_poryadok)+') '+'\t'+letters[letter_index]+ ' - ' + str(chislo) + '     ' +
        '('+str(round(chislo/all*100,2))+'%'+')')
    print('\tВсего букв: ' +str(all))


with open('text.txt') as file_object:
     #открываем фаил с текстом
     ready_text = file_object.read()
     ready_text.lower()

abc(ready_text)
#включаем функцию перебора букв в тексте

wait = input()
"""

"""
# IT WAS THE THIRD TRY//////////////////////////////////////////////////////////
from itertools import chain

letters,x,word, num= {},1,(open('text.txt', 'r')).read().replace('\n', ' ').lower(),0
print('\n Top of letters:\n')

for k in chain(range(33, 127), range(1040, 1104)): letters[chr(k)] = 0
for k in letters.keys(): letters[k] = word.count(k)
num = sum(letters.values())
for k in range(1, 11):
    arr_v, arr_k,= list(letters.values()), list(letters.keys())
    largest, index = max(arr_v), arr_v.index(max(arr_v))
    print(str(k) + ')'+ ' '*(5-len(str(k))) + arr_k[index] +\
        ' - '+str(largest)+'    (' + str(round(largest / num * 100, 2)) + '%)')
    letters[arr_k[index]] = 0
print('\n Num of words: ' + str(len(word.split(' '))))
print(' Num of letters: ' + str(num))
"""


from prettytable import PrettyTable
from itertools import chain

letters,word= {},(open('text.txt', 'r')).read().replace('\n',' ').lower()          # Создание словаря и запись текста из файла в переменную
for k in chain(range(33, 127), range(1040, 1104)): letters[chr(k)] = 0             # Цикл добавления всех нужных символов в словарь
for k in letters.keys(): letters[k] = word.count(k)                                # Подсчет кол-ва всех символов в тексте
num, table = sum(letters.values()), PrettyTable()                                  # Создание переменных кол-ва символов и таблицы для красивого вывода результатов
for k in range(1, 11):                                                             # Цикл перебора первых 10 букв по встречаемости (я гнался за минимальным размером проги)
    val, key = list(letters.values()), list(letters.keys())                        # создание списков ключей и значений основного словаря
    high, index = letters.pop(key[val.index(max(val))]), val.index(max(val))       # Создание переменных индексом самого встречаемого символа и кол-ва этого символа в тексте
    table.add_row([k,key[index]+' - '+str(high),str(round(high/num*100,2))+'%'])   # Добавление строки в таблицу для вывода с 3-мы столбцами и всеми нужными данными
print(table,'\n Words num: ',len(word.split(' ')),'\n Letters num: ', num)         # Вывод таблицы с результатами, кол-ва слов и кол-ва букв в тексте
