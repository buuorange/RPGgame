import random
import math

def calc_distancs(x1,y1,x2,y2):
    diff_x = x1-x2
    diff_y = y1-y2

    return math.sqrt(diff_x**2 + diff_y**2)

    
suika_x = random.randrange(0,5)
suika_y = random.randrange(0,5)

player_x = random.randrange(0,5)
player_y = random.randrange(0,5)

while(suika_x != player_x) or (suika_y != player_y):

    distance = calc_distancs( player_x , player_y , suika_x  ,suika_y)
    print("スイカまでの距離" , distance)

    c = input("f=東 s=西 d=南 e=北")
    if c == "f":

        player_x = player_x + 1

    elif c == "s":

        player_x = player_x - 1

    elif c == "e":

        player_y = player_y + 1

    elif c == "d":

        player_y = player_y - 1

print("スイカを割りました！")

