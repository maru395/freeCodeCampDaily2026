def find_left_handed_seat(table):
    available = 0
    for seat in table:
      for i in range(len(seat)):
          if seat[i] == "U":
              if i + 1 >= len(seat) or seat[i + 1] != "R":
                available += 1
    return available
