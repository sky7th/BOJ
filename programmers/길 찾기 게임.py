import sys
sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, nodes):
        self.data = max(nodes, key=lambda x: x['location'][1])
        self.left = None
        self.right = None
        left_nodes = list(filter(lambda x: x['location'][0] < self.data['location'][0], nodes))
        right_nodes = list(filter(lambda x: x['location'][0] > self.data['location'][0], nodes))

        if left_nodes:
            self.left = Node(left_nodes)

        if right_nodes:
            self.right = Node(right_nodes)


def solution(nodeinfo):
    nodeinfo = [{'index': idx + 1, 'location': info} for idx, info in enumerate(nodeinfo)]
    pre_orders, post_orders = [], []
    root_node = Node(nodeinfo)
    order(root_node, pre_orders, post_orders)

    return [[node['index'] for node in pre_orders], [node['index'] for node in post_orders]]


def order(node, pre_orders, post_orders):
    pre_orders.append(node.data)

    if node.left is not None:
        order(node.left, pre_orders, post_orders)

    if node.right is not None:
        order(node.right, pre_orders, post_orders)

    post_orders.append(node.data)


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
