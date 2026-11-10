class Node:
    def __init__(self, page):
        self.page = page
        self.prev = None
        self.next = None


def navigate(commands):
    current = Node("Home")

    for command in commands:
        if command.startswith("Visit "):
            new_node = Node(command[len("Visit "):])
            new_node.prev = current
            current.next = new_node      # replaces any forward history
            current = new_node
        elif command == "Back":
            if current.prev:
                current = current.prev
        elif command == "Forward":
            if current.next:
                current = current.next

    return current.page
