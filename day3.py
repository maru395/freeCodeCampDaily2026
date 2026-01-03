def find_left_handed_seat(table):
    available = 0
    for seat in table: #access elements at the table one by one
      for i in range(len(seat)): #access the index of each element
          if seat[i] == "U": 
              if i + 1 >= len(seat) or seat[i + 1] != "R": #first checks if avaible seat has no seat on its right, if it has a seat then checks if the seat next to it is right handed
                available += 1
    return available
