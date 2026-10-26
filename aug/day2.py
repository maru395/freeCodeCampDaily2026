class Node:
        def __init__(self, name):
            self.name = name
            self.next = None 

def get_food_chain(pairs):
    chain = []
    nodes = {}
    # creates one node for every unique animal (predators and foods)
    for p, f in pairs:
        nodes.setdefault(p, Node(p))
        nodes.setdefault(f, Node(f))

    # links the predator to its food node
    for p, f in pairs:
        nodes[p].next = nodes[f]

    # heads list the apex predator, the predator not found in foods
    foods = {f for _, f in pairs}
    head = next(n for name, n in nodes.items() if name not in foods)

    # travers the linked list
    cur = head
    while cur:
        chain.append(cur.name)
        cur = cur.next
    return chain  

