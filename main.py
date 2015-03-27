#!/usr/bin/env python3
from slice import Slice


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

slices = []

y = 0
for line in pizza:
    x = 0
    begin = -1
    count = 0
    for col in line:
        if col == 'H':
            if begin == -1:
                begin = x
            else:
                count += 1
        if count == 3 and (x - begin) < 12:
            slices.append(Slice((y, y), (begin, x)))
            count = 0
            begin = -1
        x += 1
    y += 1




def find_first_jambon(x, y):
    tab = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    found = []
    lvl = 1
    while lvl < S and len(found) < H:
        for i in tab:
            new_pt = (x * (i[0] * lvl), y * (i[1] * lvl))
            if new_pt in jambons:
                found.append(new_pt)
        lvl += 1
    return found


def find_first_ham(x, y):
    lvl = 1
    found = []

    def is_ham(_x, _y):
        return (_x, _y) in jambons

    found.append((x, y))
    jambons.remove((x, y))
    while lvl < S and len(found) < H:
        i = x + lvl
        j = y + lvl
        while j >= y - lvl:
            if is_ham(i, j):
                found.append((i, j))
                jambons.remove((i, j)) # A revoir
                if len(found) >= H:
                    return found
            j -= 1
            if j < y - lvl:
                j = y + lvl
                i -= 1
            if i < x - lvl:
                lvl += 1
                break

    return found

print(find_first_ham(10, 19))








#for jambon in jambons:
#




#with open("output.csv", "w") as text_file:
#    for s in servers:
#        print(s.csv(), file=text_file)

#with open("output.txt", "w") as text_file:
#    for s in servers:
#        if s._x == -1:
#            print("x", file=text_file)
#        else:
#            print("%d %d %d" % (s._y, s._x, s._group), file=text_file)

#List of slices
#slices = []

#filling with dumb data
#slices.append(Slice((1, 1), (5, 5)))
#slices.append(Slice((10, 11), (7, 8)))
#slices.append(Slice((15, 16), (12, 18)))
#slices.append(Slice((18, 19), (18, 18)))
#slices.append(Slice((21, 22), (21, 21)))

# Write the output file according to the format defined in the subject :
# first line is the number of slice
# each following line is a slice (first 2 digits are the line, last 2 digits are the columns)
def print_output(slices):
    result = open("result.txt", "w")
    length = len(slices)

    print(length)
    result.write(str(length)  + '\n')
    for slice in slices:
        slice_output = slice.get_printable_output()
        print(slice_output)
        result.write(slice_output + '\n')
    result.close()

print_output(slices)
