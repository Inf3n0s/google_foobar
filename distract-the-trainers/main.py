def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def match(graph, element, matched, found):
    for i in range(len(graph)):
        if graph[element][i] and found[i] == False:
            found[i] = True

            if matched[i] == -1 or match(graph, matched[i], matched, found):
                matched[i] = element
                return True
    return False


def check_loop(a, b):
    if a == b:
        return False
    if (a + b) % 2 == 1:
        return True
        
    k = gcd(int(a), int(b))
    a, b = a / k, b / k
    a, b = max(a, b), min(a, b)

    return check_loop(a - b, 2 * b)


def solution(banana_list):
    graph = list([0] * len(banana_list) for _ in range(len(banana_list)))
    for i in range(len(banana_list)):
        for j in range(len(banana_list)):
            if i < j:
                graph[i][j] = check_loop(banana_list[i], banana_list[j])
                graph[j][i] = graph[i][j]

    matched = [-1] * len(banana_list)
    result = 0
    for i in range(len(banana_list)):
        found = [False] * len(banana_list)
        if match(graph, i, matched, found):
            result += 1
    return int(len(banana_list) - 2 * (result / 2))


#print(solution([1, 7, 3, 21, 13, 19]))
