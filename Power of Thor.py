import sys
import math

# Solve this puzzle by writing the shortest code.
# Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
# These comments should be burnt after reading!

# lx: the X position of the light of power
# ly: the Y position of the light of power
# tx: Thor's starting X position
# ty: Thor's starting Y position
lx, ly, tx, ty = [int(i) for i in input().split()]
# game loop
while True:
    remaining_turns = int(input())  # The level of Thor's remaining energy, representing the number of moves he can still make.
    move =""
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if (ty< ly) :
        ty +=1 ;move +="S"
    elif (ty> ly):
        ty -=1; move +="N"
    if (tx> lx):
        tx -=1 ;move += "W"
    elif (tx< lx):
        tx +=1 ;move +="E"
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move)
