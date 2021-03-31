from matrix import *
from copy import deepcopy
import random




def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###     
def select_arrayBlk():
    temp = random.randrange(1, 8)
    if(temp==1):
        return arrayBlk
    elif(temp==2):
        return arrayBlk2
    elif(temp==3):
        return arrayBlk3
    elif(temp==4):
        return arrayBlk4
    elif(temp==5):
        return arrayBlk5
    elif(temp==6):
        return arrayBlk6
    elif(temp==7):
        return arrayBlk7


arrayBlk = [ [ 0, 0, 1, 0 ],
             [ 0, 0, 1, 0 ], 
             [ 0, 0, 1, 0 ], 
             [ 0, 0, 1, 0 ] ]

arrayBlk2 = [[ 0, 0, 1, 0 ],
             [ 0, 0, 1, 0 ], 
             [ 0, 1, 1, 0 ], 
             [ 0, 0, 0, 0 ] ]

arrayBlk3 = [[ 0, 1, 0, 0 ],
             [ 0, 1, 0, 0 ], 
             [ 0, 1, 1, 0 ], 
             [ 0, 0, 0, 0 ] ]

arrayBlk4 = [[ 0, 0, 0, 0 ],
             [ 0, 1, 1, 0 ], 
             [ 0, 1, 1, 0 ], 
             [ 0, 0, 0, 0 ] ]

arrayBlk5 = [[ 0, 0, 0, 0 ],
             [ 0, 1, 1, 0 ], 
             [ 1, 1, 0, 0 ], 
             [ 0, 0, 0, 0 ] ]

arrayBlk6 = [[ 0, 0, 0, 0 ],
             [ 0, 1, 1, 1 ], 
             [ 0, 0, 1, 0 ], 
             [ 0, 0, 0, 0 ] ]

arrayBlk7 = [[ 0, 0, 0, 0 ],
             [ 0, 1, 1, 0 ],
             [ 0, 0, 1, 1 ],
             [ 0, 0, 0, 0 ] ]

arrayBlk = select_arrayBlk()



def rotate(arrayBlk):
    column , row = 4,4
    tempBlk2 = [[0 for _ in range(row)] for _ in range(column)]
    for i in range(0,4):
        for j in range(0,4):
            tempBlk2[i][j] = arrayBlk[i][j]

    for i in range(0,4):
        for j in range(0,4):
            arrayBlk[j][3-i] = tempBlk2[i][j]
     
    return arrayBlk 
    
    
### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        arrayBlk = rotate(arrayBlk)
        currBlk = Matrix(arrayBlk)
        continue
    elif key == ' ': # drop the block
        
        while(True):
            top += 1
            tempBlk = iScreen.clip(
                top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            if tempBlk.anyGreaterThan(1):
               break

    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            arrayBlk = rotate(-1)
            currBlk = Matrix(arrayBlk)
        elif key == ' ': # undo: move up
            top -= 1
            newBlockNeeded = True

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        arrayBlk = select_arrayBlk()
        currBlk = Matrix(arrayBlk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
