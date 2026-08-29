# used doubly circular linked list and bfs

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
    def __init__(self, values):
        self.head = Node(values[0])
        current = self.head
        for value in values[1:]:
            new_node = Node(value)
            current.next = new_node
            new_node.prev = current
            current = new_node
        current.next = self.head
        self.head.prev = current

    def find(self, value):
        current = self.head
        while True:
            if current.value == value:
                return current
            current = current.next
            if current is self.head:
                return None


ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

COMPATIBILIT_TABLE = {
    0: "100%",
    1: "40%",
    2: "80%",
    3: "30%",
    4: "90%",
    5: "20%",
    6: "50%"
}

zodiac = DoublyCircularLinkedList(ZODIAC_SIGNS)  


def horoscope_match(sign1, sign2):
    start = zodiac.find(sign1)          
    if start is None:
        raise ValueError(f"{sign1} not found")
    if sign1 == sign2:
        return COMPATIBILIT_TABLE[0]

    visited = {id(start)}
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        for neighbor in (node.next, node.prev):
            if neighbor.value == sign2:
                return COMPATIBILIT_TABLE[dist + 1]
            if id(neighbor) not in visited:
                visited.add(id(neighbor))
                queue.append((neighbor, dist + 1))

    return -1
