from itertools import islice
import sys
users = []
hobby = []

gen_line = (line for line in open('users.csv'))
for line in islice(gen_line, None):
    line = line.replace("\n", '')
    users.append(line)


gen_line = (line for line in open('hobby.csv'))
for line in islice(gen_line, None):
    line = line.replace("\n", '')
    hobby.append(line)


if len(hobby) < len(users):
    hobby.append(None)
elif len(hobby) > len(users): # выход с кодом 1 по условию задания
    sys.exit(1)               #


sum = dict(zip(users, hobby))
for k, v in sum.items():
    print(f'{k}:  {v}')

with open('result_file.csv','w') as rf:
    for key,val in sum.items():
        rf.write('{}: {}\n'.format(key,val))

print('\n ПРОВЕРЯЕМ НОВЫЙ ФАЙЛ result_file.csv\n ')
with open('result_file.csv','r') as rf:
    print(rf.read())



