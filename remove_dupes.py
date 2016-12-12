import os

directory = ''
delete = [f for f in os.listdir(directory) if '(1)' in f]

for d in delete:
    os.remove(directory + '/{}'.format(d))

