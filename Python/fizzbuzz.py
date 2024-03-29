"""
Just for fun, I solve FizzBuzz in several different ways.
"""

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)


for i in range(1, 100):
    if i % 3 and i % 5:
        print(i)
    elif i % 3:
        print('buzz')
    elif i % 5:
        print('fizz')
    else:
        print(i)

for i in range(1, 100):
    print((i if i % 3 else 'fizz') if i % 5 else ('buzz' if i % 3 else 'fizzbuzz'))

for i in range(1, 100):
    print((i if i % 3 else 'fizz') if i % 5 else ('buzz' if i % 3 else 'fizzbuzz'))

for i in range(1, 100):
    print([['fizzbuzz', 'fizz'], ['buzz', i]][bool(i % 3)][bool(i % 5)])  # type: ignore

for i in range(1, 100):
    print([[i, 'buzz'], ['fizz', 'fizzbuzz']][i % 3 == 0][i % 5 == 0])  # type: ignore

[print([[i, 'buzz'], ['fizz', 'fizzbuzz']][i % 3 == 0][i % 5 == 0]) for i in range(1, 100)]  # type: ignore
