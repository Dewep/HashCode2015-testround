__author__ = 'Steven'


# 0 dispo
# 1 indispo
# 2 serveur

class Datacenter(object):
    def __init__(self, rows, cols):
        self._map = []
        self._rows = rows
        self._cols = cols
        for i in range(0, rows):
            self._map.append([0 for i in range(0, cols)])

        print("Rows: %s" % len(self._map))


    def setAvailability(self, x, y):
        self._map[y][x] = 1

    def showMap(self):
        print("lines: %s" % (len(self._map)))
        for line in self._map:
            print("%s: %s" % (len(line), "".join([str(o) for o in line])))

    def isEmpty(self):
        ret = 0
        for line in self._map:
            ret += line.count(0)
        return ret

    def getLowestLine(self, servers, exclude):
        lines = []
        for i in range(0, len(self._map)):
            lines.append(0)
        for server in servers:
            if server._y >= 0:
                lines[server._y] += server._power
        #print(str(lines))
        lowest_line = 0
        lowest_value = lines[0]
        for i in range(0, len(self._map)):
            value = lines[i]
            if value < lowest_value and i not in exclude:
                lowest_line = i
                lowest_value = value
        #print(lowest_line)
        return lowest_line


#    def getLowestLine(self):
#        lowest_line = 0
#        lowest_value = self._map[0].count(0)
#        for i in range(0, len(self._map)):
#            value = self._map[i].count(2)
#            print("%s:%s" % (i, value))
#            if value < lowest_value:
#                lowest_line = i
#                lowest_value = value
#        print(lowest_line)
#        return lowest_line
#        #return lowest_group
#        #for line in self._map:
#        #    ret += line.count(0)

    def storeInLine(self, line, server, servers, nb_groups):
        s = "%0*d" % (server._size, 0)
        #print(s)
        line_str = "".join([str(o) for o in self._map[line]])
        pos = line_str.find(s)
        if pos >= 0:
            for i in range(0, server._size):
                if self._map[line][pos + i] != 0:
                    raise Exception("Euh !!! line(%s), pos(%s): " % (line, pos + i))
                self._map[line][pos + i] = 2
            server._x = pos
            server._y = line
            server._group = getLowestGroup(servers, nb_groups, line)
            #if server._group == -1:
            #    server._group = getLowestGroup(servers, nb_groups)
            # attribuer groupe
            return True
        return False




class Server(object):
    def __init__(self, line, size, power):
        self._x = -1
        self._y = -1
        self._group = -1
        self._size = int(size)
        self._power = int(power)
        self._line = int(line)

    def __str__(self):
        return "%s: x(%s), y(%s), group(%s), ratio(%s), power(%s), size(%s)" % (self._line, self._x, self._y, self._group, self.getPerf(), self._power, self._size)

    def csv(self):
        return "%d;%d;%d;%d;%d;%d;%d" % (self._line, self._x, self._y, self._group, self.getPerf(), self._power, self._size)

    def setPosXY(self, x, y):
        self._x = x
        self._y = y

    def getPerf(self):
        return self._power / self._size

    def __cmp__(self, o):
        if self.getPerf() < o.getPerf():
            return -1
        if self.getPerf() > o.getPerf():
            return 1
        if self._size > o._size:
            return -1
        if self._size < o._size:
            return 1
        return 0
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    def __le__(self, other):
        return self.__cmp__(other) <= 0
    def __ge__(self, other):
        return self.__cmp__(other) >= 0
    def __ne__(self, other):
        return self.__cmp__(other) != 0


def guaranteedCapacity(datacenter, servers):
    rows = []
    for i in range(0, datacenter._rows):
        rows.append(999)
    for s in servers:
        if s._x != -1:
            rows[s._y] = min(rows[s._y], s._power)
    return min(*rows)


def groupByGroup(servers, nb_groups, line):
    groups = []
    for i in range(0, nb_groups):
        groups.append([])
    for s in servers:
        if s._group != -1 and (line is None or s._y == line):
            groups[s._group].append(s)
    return groups


def getPowerByGroup(servers, nb_groups, line):
    groups = groupByGroup(servers, nb_groups, line)
    powers = []
    for i in range(0, nb_groups):
        value = 0
        for s in groups[i]:
            value += s._power
        powers.append(value)
    return powers


def getLowestGroup(servers, nb_groups, line=None, only_in=None):
    groups = getPowerByGroup(servers, nb_groups, line)
    lowest_group = 0
    lowest_value = 999999
    for i in range(0, nb_groups):
        if groups[i] < lowest_value and (not only_in or i in only_in):
            lowest_group = i
            lowest_value = groups[i]
    equals = []
    if line:
        for i in range(0, nb_groups):
            if groups[i] == lowest_value:
                equals.append(i)
        if len(equals) == 1:
            return equals[0]
        return getLowestGroup(servers, nb_groups, only_in=equals)
    return lowest_group


def getLowestGroupLine(servers, line, nb_groups):
    groups = []
    for i in range(0, nb_groups):
        groups.append([])
    for s in servers:
        if s._group != -1 and s._y == line:
            groups[s._group].append(s)
    powers = []
    for i in range(0, nb_groups):
        value = 0
        for s in groups[i]:
            value += s._power
        powers.append(value)
    lowest_group = 0
    lowest_value = 999999
    for i in range(0, nb_groups):
        if powers[i] < lowest_value:
            lowest_group = i
            lowest_value = powers[i]
    return lowest_group
