def parse_number(i):
    points = i.count('.')  # count the number of points in version
    if (points == 0):
        return [int(i), -1, -1]
    elif (points == 1):
        return [int(i[:i.find('.')]), int(i[i.find('.')+1:]), -1]
    elif (points == 2):
        return [int(i[:i.find('.')]), int(i[i.find('.')+1:i.rfind('.')]), int(i[i.rfind('.')+1:])]


def solution(l):
    v = []
    for i in l:
        v.append(parse_number(i))

    # sort a array by the a[0],a[1],a[2]
    v = sorted(v, key=lambda a: (a[0], a[1], a[2]))
    rez = []

    for i in v:
        r = str(i[0])
        if (i[1] != -1):
            r += '.' + str(i[1])
        if (i[2] != -1):
            r += '.' + str(i[2])
        rez.append(r)

    return rez


#print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])) 
#print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
#print(solution(["1.30", "0.1", "1.3.0", "0.1.30", "12.0.223"]))