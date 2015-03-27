#!/usr/bin/env python3
from datetime import datetime

from objects import Datacenter, Server, guaranteedCapacity

R, S, U, P, M = map(int, input().split())

servers = []
datacenter = Datacenter(R, S)

for i in range(0, U):
    y, x = map(int, input().split())
    datacenter.setAvailability(x, y)

datacenter.showMap()

for i in range(0, M):
    x, y = map(int, input().split())
    servers.append(Server(i, x, y))


sort = sorted(servers, reverse=True)

for s in sort:
    print(str(s))

_round = 1500
#_round = 1
while datacenter.isEmpty() > 0 and _round >= 0:
    print(_round)
    exclude = []
    while len(exclude) < R:
        line = datacenter.getLowestLine(servers, exclude)
        exclude.append(line)
        j = 0
        while j < len(sort):
            if datacenter.storeInLine(line, sort[j], servers, P):
                del sort[j]
                break
            else:
                j += 1
    _round -= 1
    #if j == len(sort):
    #    print("try exhausted in this line")
    #    continue
            #print("store in %s: %s" % (i, ))

    #for i in range(0, datacenter._rows):
    #    j = 0
    #    if datacenter.storeInLine(i, sort[0], servers, P):
    #        del sort[j]
    #    else:
    #        j += 1
    #    if j == len(sort):
    #        print("try exhausted in this line")
    #        continue
    #    #print("store in %s: %s" % (i, ))


datacenter.showMap()
#sorted(servers, key=lambda o: o._line)

for s in servers:
    print(str(s))
datacenter.showMap()
print(guaranteedCapacity(datacenter, servers))


with open("output.csv", "w") as text_file:
    for s in servers:
        print(s.csv(), file=text_file)

with open("output.txt", "w") as text_file:
    for s in servers:
        if s._x == -1:
            print("x", file=text_file)
        else:
            print("%d %d %d" % (s._y, s._x, s._group), file=text_file)
