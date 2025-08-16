import random

# random.setstate(42)
r = random.random()
print(r)
print(random.random())
print(random.randint(1,10))
print(random.uniform(1,10))
print(random.randrange(1,10))
print(random.choice([1,2,3,4,5]))
print(random.choices([1,2,3,4,5],k=3))
print(random.sample([1,2,3,4,5],k=3))
print(random.shuffle([1,2,3,4,5]))
print(random.seed(0))
# print(random.getstate())

'''
ubuntu@VM-8-12-ubuntu:~/repo/algo$ python A2_generateRandom.py 
0.31777507384917947
0.31964600318407066
2
3.086082762553782
4
3
[1, 5, 4]
[1, 4, 2]
None
None
'''