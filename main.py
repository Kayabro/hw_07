#
# string = 'пара-ра-рам рам-пам-папам па-ра-па-да '
#
# def search_a(text):
#     text = text.split()
#     counter_a = []
#
#     for i in text:
#         counter_a.append(i.count('а'))
#
#     for i in range(1, len(counter_a)):
#         if counter_a[i - 1] != counter_a[i]:
#             return ('Пам парам')
#     else:
#         return ("Парам пам-пам")
#
# print(search_a(string))

# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
# 1         2         3         4         5          6
# 2         4         6         8         10         12
# 3         6         9         12        15         18
# 4         8        12         16        20         24
# 5        10        15         20        25         30
# 6        12        18         24        30         36


def print_operation_table(operation, numRows=6, numColumns=6):
    for row in range(1, numRows+1):
        for column in range(1, numColumns+1):
            print(operation(row,column), end='\t')
        print()

print_operation_table(lambda x, y: x * y, 6, 6)