# FILE I/O
# from pathlib import Path
from translate import Translator

translator = Translator(to_lang="tl")

# p = Path('.')
# q = p / 'test' / 'test.txt'
# my_list = p.is_dir()

# with q.open() as f:
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

try:
    with open('test/test.txt', mode='r') as my_file:
        text = my_file.readline()
        translation = translator.translate(text)
        # print(translation)
        with open('test/test-tagalog.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('check your file path.')
