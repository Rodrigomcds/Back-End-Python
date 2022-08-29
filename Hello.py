

def my_gen():

    n = 1
    print('Primeiro print n = {}'.format(n))
    yield n

    n += 1
    print('Segundo print n = {}'.format(n))
    yield n

    n += 1
    print('Terceiro e ultimo print n = {}'.format(n))
    yield n


test = my_gen()

v = 0

while True:
    a = next(test)
    v += 1
