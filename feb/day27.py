from collections import deque

def shift_matrix(matrix, shift):
    flatten = [item for sublist in matrix for item in sublist]
    mdeque = deque(flatten)
    # if number is positive
    if shift > 0:
        temp = flatten[-shift:]
        temp = temp[::-1]
        for _ in range(shift):
            mdeque.pop()
        for i in range(len(temp)):
            mdeque.appendleft(temp[i])
    # if number us negative
    else:
        temp = flatten[:abs(shift)]
        temp = temp[::-1]
        for _ in range(abs(shift)):
            mdeque.popleft()
        for i in range(len(temp)):
            mdeque.append(temp[i])
    # turning it into matrix
    flattened_list = [i for i in mdeque]
    columns = len(matrix[0])

    # List comprehension to chunk the list
    original_list_of_lists = [flattened_list[i:i + columns] for i in range(0, len(flattened_list), columns)]
    return original_list_of_lists
