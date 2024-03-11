import os
import pprint
directory = os.getcwd()
content = os.listdir(directory)
txt = []
new_file = {}
for files in content:
    if os.path.isfile(os.path.join(directory, files)) and files.endswith('.txt'):
        txt.append(files)
for file in txt:
    with (open(file, 'r', encoding='UTF-8') as f):
        count = 0
        direct = {}
        for line in f.read().split('\n'):
            count += 1
            direct.update(dict({count: line}))
        new_file.update(dict({file: direct}))

pprint.pprint(new_file)

new_txt = open('new.txt', 'a', encoding='UTF-8')
for key_1, value_1 in new_file.items():
    new_txt.write(key_1 + "\n")
    new_txt.write(str(max(value_1.keys())) + "\n")
    for key, value in value_1.items():
        if key <= 2:
            new_txt.write(value + "\n")

new_txt.close()
