def is_fizz_buzz(arr):
    temp = 0
    counter = 0
    expected_arr = []

    for x in range(len(arr)):
        if isinstance(arr[x], int):
            temp = arr[x]
            break
        else:
            counter -= 1

    for x in range(len(arr)):
        expected_arr.append(temp + counter)
        counter += 1

    for x in range(len(arr)):
        if expected_arr[x] % 15 == 0:       
            if arr[x] != "FizzBuzz":
                return False
        elif expected_arr[x] % 3 == 0:      
            if arr[x] != "Fizz":
                return False
        elif expected_arr[x] % 5 == 0:      
            if arr[x] != "Buzz":
                return False
        else:
            if arr[x] != expected_arr[x]:   
                return False

    return True
