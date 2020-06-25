from collections import defaultdict

answer = []


def solution(tickets):
    graph = defaultdict(list)

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for key in graph.keys():
        graph[key].sort()

    dfs(graph, "ICN", ["ICN"])

    return answer


def dfs(graph, key, route):
    if len(graph[key]) == 0:
        if isEmptyTicket(graph):
            answer.append(route)
        return

    for idx, country in enumerate(graph[key]):
        r = route[:]
        r.append(graph[key].pop(idx))
        dfs(graph, country, r)
        graph[key].insert(idx, country)


def isEmptyTicket(graph):
    for key in graph.keys():
        if len(graph[key]) != 0:
            return False

    return True


print(solution( [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]))
