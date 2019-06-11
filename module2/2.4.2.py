
'''Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя
бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
Пример архива
Пример ответа'''


import os
import os.path
lst = []
with open("res.txt", "w") as result, open("newres.txt", "w") as new:
    for current_dir, dirs, files in os.walk("main"):
        for file in files:
            if file.endswith(".py"):
                result.write(current_dir)
                result.write("\n")
                break
    
with open("res.txt", "r") as file, open("newres.txt", "w") as new:
    for line in file:
        lst.append(line)
    for i in sorted(lst):
        new.write(i)

