import random 
randomlist = []
d = 500000
for i in range(d):
  randomlist.append(random.randint(0, d))

ordem = int(input('''
Digite a ordem da lista
[1] - para ordem crescente
[2] - para ordem decrescente
'''))

if ordem == 1 :
  randomlist.sort()
else:
  randomlist.sort(reverse=True)

print(randomlist)
