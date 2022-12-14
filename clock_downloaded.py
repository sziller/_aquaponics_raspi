from sense_hat import SenseHat
import datetime
import time

td_in_h = -1  # Time difference between Raspberry time and Actual time in hours > tR - tA
td_in_m = 0  # Time difference between Raspberry time and Actual time in minutes > tR - tA

sense = SenseHat()
sense.low_light = True
sense.rotation = 90

# unit: 60/29
u = 60.0/29

numbers = {0:   [[0,0,1,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,1,1,0,0]],
           1:   [[0,0,0,1,0,0],[0,0,1,1,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,1,1,1,0]],
           2:   [[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,0,0,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,1,1,1,1,0]],
           3:   [[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,1,0,0,1,0],[0,0,1,1,0,0]],
           4:   [[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,1,0,1,0],[0,1,1,1,1,0],[0,0,0,0,1,0],[0,0,0,0,1,0]],
           5:   [[0,1,1,1,1,0],[0,1,0,0,0,0],[0,1,1,1,0,0],[0,0,0,0,1,0],[0,1,0,0,1,0],[0,0,1,1,0,0]],
           6:   [[0,0,1,1,0,0],[0,1,0,0,0,0],[0,1,1,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,1,1,0,0]],
           7:   [[0,1,1,1,1,0],[0,0,0,0,1,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,0,1,0,0,0]],
           8:   [[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,1,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,1,1,0,0]],
           9:   [[0,0,1,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,1,1,1,0],[0,0,0,0,1,0],[0,0,1,1,0,0]],
           10:  [[0,1,0,0,1,0],[1,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,0,1,0]],
           11:  [[0,1,0,0,1,0],[1,1,0,1,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,0,1,0]],
           12:  [[0,1,0,0,1,0],[1,1,0,1,0,1],[0,1,0,0,0,1],[0,1,0,0,1,0],[0,1,0,1,0,0],[0,1,0,1,1,1]],
           13:  [[0,1,0,1,1,1],[1,1,0,0,0,1],[0,1,0,0,1,0],[0,1,0,0,0,1],[0,1,0,1,0,1],[0,1,0,0,1,0]],
           14:  [[0,1,0,1,0,0],[1,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,1,1,1],[0,1,0,0,0,1],[0,1,0,0,0,1]],
           15:  [[0,1,0,1,1,1],[1,1,0,1,0,0],[0,1,0,1,1,0],[0,1,0,0,0,1],[0,1,0,1,0,1],[0,1,0,0,1,0]],
           16:  [[0,1,0,0,1,1],[1,1,0,1,0,0],[0,1,0,1,1,0],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,0,1,0]],
           17:  [[0,1,0,1,1,1],[1,1,0,0,0,1],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,1,0,1,0,0],[0,1,0,1,0,0]],
           18:  [[0,1,0,0,1,0],[1,1,0,1,0,1],[0,1,0,0,1,0],[0,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,0,1,0]],
           19:  [[0,1,0,0,1,0],[1,1,0,1,0,1],[0,1,0,1,0,1],[0,1,0,0,1,1],[0,1,0,0,0,1],[0,1,0,1,1,0]],
           20:  [[0,1,0,0,1,0],[1,0,1,1,0,1],[0,0,1,1,0,1],[0,1,0,1,0,1],[1,0,0,1,0,1],[1,1,1,0,1,0]],
           21:  [[0,1,0,0,1,0],[1,0,1,1,1,0],[0,0,1,0,1,0],[0,1,0,0,1,0],[1,0,0,0,1,0],[1,1,1,0,1,0]],
           22:  [[0,1,0,0,1,0],[1,0,1,1,0,1],[0,0,1,0,0,1],[0,1,0,0,1,0],[1,0,0,1,0,0],[1,1,1,1,1,1]],
           23:  [[0,1,0,1,1,1],[1,0,1,0,0,1],[0,0,1,0,1,0],[0,1,0,0,0,1],[1,0,0,1,0,1],[1,1,1,0,1,0]]}

numbers_8x8 = {0:   [[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
               1:   [[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0]],
               2:   [[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,1,1,1,0,0],[0,0,0,0,0,0,0,0]],
               3:   [[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
               4:   [[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,1,0,0],[0,0,0,1,0,1,0,0],[0,0,1,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0]],
               5:   [[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
               6:   [[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
               7:   [[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0]],
               8:   [[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
               9:   [[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
              10:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,0]],
              11:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,1,0,1,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,0]],
              12:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,1,0,1,0,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,1,0,1,0,0,0],[0,0,1,0,1,1,1,0],[0,0,0,0,0,0,0,0]],
              13:  [[0,0,0,0,0,0,0,0],[0,0,1,0,1,1,1,0],[0,1,1,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,0]],
              14:  [[0,0,0,0,0,0,0,0],[0,0,1,0,1,0,0,0],[0,1,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,1,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0]],
              15:  [[0,0,0,0,0,0,0,0],[0,0,1,0,1,1,1,0],[0,1,1,0,1,0,0,0],[0,0,1,0,1,1,0,0],[0,0,1,0,0,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,0]],
              16:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,1,0],[0,1,1,0,1,0,0,0],[0,0,1,0,1,1,0,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,0]],
              17:  [[0,0,0,0,0,0,0,0],[0,0,1,0,1,1,1,0],[0,1,1,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0]],
              18:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,1,0,1,0,1,0],[0,0,1,0,0,1,0,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,0,0,0,0,0]],
              19:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,0,1,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,1,1,0,0],[0,0,0,0,0,0,0,0]],
              20:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,0,1,1,0,1,0],[0,0,0,1,1,0,1,0],[0,0,1,0,1,0,1,0],[0,1,0,0,1,0,1,0],[0,1,1,1,0,1,0,0],[0,0,0,0,0,0,0,0]],
              21:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,0,1,1,1,0,0],[0,0,0,1,0,1,0,0],[0,0,1,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,1,1,0,1,0,0],[0,0,0,0,0,0,0,0]],
              22:  [[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,1,0,1,1,0,1,0],[0,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0]],
              23:  [[0,0,0,0,0,0,0,0],[0,0,1,0,1,1,1,0],[0,1,0,1,0,0,1,0],[0,0,0,1,0,1,0,0],[0,0,1,0,0,0,1,0],[0,1,0,0,1,0,1,0],[0,1,1,1,0,1,0,0],[0,0,0,0,0,0,0,0]]}

perimeter = [[24,25,26,27,0,1,2,3],[23,0,0,0,0,0,0,4],[22,0,0,0,0,0,0,5],[21,0,0,0,0,0,0,6],[20,0,0,0,0,0,0,7],[19,0,0,0,0,0,0,8],[18,0,0,0,0,0,0,9],[17,16,15,14,13,12,11,10]]

# hour background color
z = [0,0,0]

# hour number color
w = [255,255,255]

# minute background color
e = [0,0,0]

# minute dot color
x = [0,255,0]

def row_one(m):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    if m > u * 4 and m < u * 25:
        result = [0, 0, 0, 0, 1, 1, 1, 1]
    else:
        if m < u:
            result = [0, 0, 0, 0, 0, 0, 0, 0]
        elif m < u * 2:
            result = [0, 0, 0, 0, 1, 0, 0, 0]
        elif m < u * 3:
            result = [0, 0, 0, 0, 1, 1, 0, 0]
        elif m < u * 4:
            result = [0, 0, 0, 0, 1, 1, 1, 0]
        elif m < u * 25:
            result = [0, 0, 0, 0, 1, 1, 1, 1]
        elif m < u * 26:
            result = [1, 0, 0, 0, 1, 1, 1, 1]
        elif m < u * 27:
            result = [1, 1, 0, 0, 1, 1, 1, 1]
        elif m < u * 28:
            result = [1, 1, 1, 0, 1, 1, 1, 1]
        else:
            result = [1, 1, 1, 1, 1, 1, 1, 1]
    return result

def row_eight(m):
    result = [1, 1, 1, 1, 1, 1, 1, 1]
    if m < u * 18:
        if m < u * 11:
            result = [0, 0, 0, 0, 0, 0, 0, 0]
        elif m < u * 12:
            result = [0, 0, 0, 0, 0, 0, 0, 1]
        elif m < u * 13:
            result = [0, 0, 0, 0, 0, 0, 1 ,1]
        elif m < u * 14:
            result = [0, 0, 0, 0, 0, 1, 1, 1]
        elif m < u * 15:
            result = [0, 0, 0, 0, 1, 1, 1, 1]
        elif m < u * 16:
            result = [0, 0, 0, 1, 1, 1, 1, 1]
        elif m < u * 17:
            result = [0, 0, 1, 1, 1, 1, 1, 1]
        else:
            result = [0, 1, 1, 1, 1, 1, 1, 1]
    return result

def logical_list_entry_substitute(list_in, false, true):
    '''converts logical lists entries into entries
    represented by "false" or "true"'''
    return [false if _ == 0 else true for _ in list_in]
        

def update_clock(hh, mm):
    img = []
    
    # row 1
    row1 = row_one(mm)
    img.extend(logical_list_entry_substitute(row1, e, x))

    # row 2-7
    for i in range(6):
        if mm > (u * (24 - i)):
            img.append(x)
        else:
            img.append(e)

        # hour number
        img.extend(logical_list_entry_substitute(numbers[hh][i], z, w))

        if mm > (u *(5 + i)):
            img.append(x)
        else:
            img.append(e)
    #row 8
    row8 = row_eight(mm)
    img.extend(logical_list_entry_substitute(row8, e, x))
    for _ in img:
        print(_)
    sense.set_pixels(img)

try:
    while True:
        now = datetime.datetime.now()
        hour = now.hour - td_in_h
        if hour > 23:
            hour = hour - 24
        minute = (now.minute - td_in_m)*1.0
        if minute > 59:
            minute = minute - 60
        
        update_clock(hour, minute)
        time.sleep(10)
except KeyboardInterrupt:
    print ('Closed.')
    sense.clear()
