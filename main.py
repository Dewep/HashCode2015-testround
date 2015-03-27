#!/usr/bin/env python3


pizza = []

jambons = [] # tableau de tuples (x, y) : ou y == line


# liste des parts là où il y a du jambon
# récupérer le jambon le plus proche, puis le plus proche de l'autre
# puis du détermine le carré

with open("test_round.in", "r") as f:
    R, C, H, S = map(int, f.readline().split())
    print("%s %s %s %s" % (R, C, H, S))
    for line in f:
        l = line.replace('\r', '').replace('\n', '')
        print("[%s]" % l)
        pizza.append(l)

print("pizza lines %s, cols %s" % (len(pizza), len(pizza[0])))

y = 0
for line in pizza:
    x = 0
    for col in line:
        if col == 'H':
            obj = (x, y)
            jambons.append(obj)
        x += 1
    y += 1

print(str(jambons))
print("Nb jambons %s" % len(jambons))

# x = colonne
# y = ligne


jambons = [(1, 1), (2, 1), (3, 1)]


def find_first_jambon(x, y):
    tab = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    found = []
    lvl = 1
    while lvl < H and len(found) == 0:
        for i in tab:
            new_pt = (x * (i[0] * lvl), y * (i[1] * lvl))
            if new_pt in jambons:
                found.append(new_pt)
        lvl += 1
    return found





#with open("output.csv", "w") as text_file:
#    for s in servers:
#        print(s.csv(), file=text_file)

#with open("output.txt", "w") as text_file:
#    for s in servers:
#        if s._x == -1:
#            print("x", file=text_file)
#        else:
#            print("%d %d %d" % (s._y, s._x, s._group), file=text_file)
