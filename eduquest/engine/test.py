import pathlib

path = pathlib.Path('eduquest.sqlite')
print(path.exists())  # True
print(path.is_file())  # True

if not path.exists():
    print('ok')
else:
    print('файла нет')