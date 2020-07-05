# l = [i for i in range(10) if i % 2 == 0]

# print(l)

# d = {i: " hello" for i in range(10) if i % 2 == 0}
# print(d)

g = (i for i in range(10))

# print(f'next: {g.__next__}')

print(f'next: {g.__next__()}')
print('-' * 10)
for i in g:
    print(i)
