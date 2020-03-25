from collections import deque

def DFS(start_node, graph_dict, total_visit):
    visit = []  # total_visit ������ ��� ��, ���� start_node ���� DFS�� ������ ������ ����Ʈ
    stack = deque()
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in total_visit:
            visit.append(node)
            total_visit.append(node)
            for child_i in graph_dict[node]:
                if child_i not in total_visit:
                    stack.append(child_i)

    return visit

def solution(n, computers):
    
    # 1. graph_dict �����
    graph_dict = {}
    for i in range(n):  # 0 ~ (n-1)�� ���
        graph_dict[i] = []
    for r_i in range(n):
        for c_i in range(n):
            if r_i == c_i:
                continue
            elif computers[r_i][c_i] == 1:
                graph_dict[r_i].append(c_i)
    
    # 2.1. DFS
    group_count = 0
    remain_nodes = list(range(n))  # 0 ~ n-1
    total_visit = []
    visit = DFS(0, graph_dict, total_visit)
    for visit_i in visit:
        remain_nodes.remove(visit_i)
    group_count += 1
    
    # 2.2. visit �� ���� node �� �ٽ� DFS => while (len(visit == n))
    while len(remain_nodes) > 0:
        visit = DFS(remain_nodes[0], graph_dict, total_visit)
        for visit_i in visit:
            remain_nodes.remove(visit_i)
        group_count += 1
    
    return group_count