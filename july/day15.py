def chunk_array(arr, size):
    main_arr = []
    counter = 0
    sub_arr = []
    for x in arr:
        if counter == size:
            main_arr.append(sub_arr)
            counter = 0
            sub_arr = []
        sub_arr.append(x)
        counter += 1

    if sub_arr:
        main_arr.append(sub_arr)

    return main_arr
