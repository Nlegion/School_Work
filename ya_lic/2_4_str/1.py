# Формат ввода
# Вводится количество играющих, затем строки, в которых могут быть их имена. Затем вводится количество имен и сами имена детей для поиска.
#
# Формат вывода
# Для каждого имени выведите номер строки (счет с 1), в которой оно первый раз встретилось, или -1, если такого имени не было.

st1 = int(input())

st_list = []
name_list = []
score = 0
for item in range(st1):
    st_list.append(input())

st2 = int(input())
for item in range(st2):
    name_list.append(input())

for itr_2 in name_list:
    for itr in range(len(st_list)):
        if itr_2 in st_list[itr]:
            print(itr + 1)
            break
        else:
            score += 1
    if score == len(st_list):
        print(-1)
    score = 0
