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


#
#
# def print_operation_table(operation, numRows, numColumns):
#     for row in range(1, numRows+1):
#         for column in range(1, numColumns+1):
#             print(operation(row,column), end='\t')
#         print()
#
# print_operation_table(lambda x, y: x * y, 6, 6)
