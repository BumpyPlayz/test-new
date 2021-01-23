import pyautogui
from PIL import Image
import os
import cv2
import random

folder = 'Photos'

def click(pos1, pos2):
    pyautogui.click(pos1, pos2)

def check(index, alltiles, width, height):
    toreturn = []
    totalblocks = width*height
    if (index < width):
        if (index == 0):
            toreturn = [alltiles[1], alltiles[width], alltiles[width+1]]
        elif (index == (width-1)):
            toreturn = [alltiles[width-2], alltiles[(width-1)*2], alltiles[((width-1)*2)+1]]
        else:
            toreturn = [alltiles[index-1], alltiles[index+1], alltiles[index+width-1], alltiles[index+width], alltiles[index+width+1]]
    elif (index > (totalblocks-width-1)):
        if (index == (totalblocks-width)):
            toreturn = [alltiles[totalblocks-width-width], alltiles[totalblocks-width-width+1], alltiles[totalblocks-width+1]]    
        elif (index == (totalblocks-1)):
            toreturn = [alltiles[totalblocks-width-2], alltiles[totalblocks-width-1], alltiles[totalblocks-2]]
        else:
            toreturn = [alltiles[index+1], alltiles[index-1], alltiles[index-totalblocks+1], alltiles[index-totalblocks], alltiles[index-totalblocks-1]]
    else:
        if (index%width == 0):
            toreturn = [alltiles[index-width], alltiles[index-width+1], alltiles[index+1], alltiles[index+width], alltiles[index+width+1]]
        elif (index%width == (width-1)):
            toreturn = [alltiles[index-width], alltiles[index-width-1], alltiles[index-1], alltiles[index+width-1], alltiles[index+width]]
        else:
            toreturn = [alltiles[index-width-1], alltiles[index-width], alltiles[index-width+1], alltiles[index-1], alltiles[index+1], alltiles[index+width-1], alltiles[index+width], alltiles[index+width+1]]

    return toreturn

def LoadImages():
    TILES = {
        '_': cv2.imread(os.path.join(folder,'none.png'), 0),
        0: cv2.imread(os.path.join(folder,'0.png'), 0),
        1: cv2.imread(os.path.join(folder,'1.png'), 0),
        2: cv2.imread(os.path.join(folder,'2.png'), 0),
        3: cv2.imread(os.path.join(folder,'3.png'), 0),
        4: cv2.imread(os.path.join(folder,'4.png'), 0),
        5: cv2.imread(os.path.join(folder,'5.png'), 0),
        6: cv2.imread(os.path.join(folder,'6.png'), 0),
        7: cv2.imread(os.path.join(folder,'7.png'), 0),
        8: cv2.imread(os.path.join(folder,'8.png'), 0),
        'M': cv2.imread(os.path.join(folder,'mine.png'), 0),
        'F': cv2.imread(os.path.join(folder,'flag.png'), 0)
        }
    return TILES


def process(height, width, TILES):
    while (True):
        WON = False
        guessing = True
        Dead = False
        while (True):
            if (Dead == True):
                guessing = True
                Dead = False
            all_tiles = []
            blockmove = False
            for tile in TILES:
                positions = pyautogui.locateAllOnScreen(TILES[tile], confidence = 0.98, grayscale=True)
                for p in positions:
                    all_tiles.append({'value':tile, 'position': p})

            all_tiles = sorted(all_tiles, key=lambda x:(x['position'][1], x['position'][0]))
        
            for i, tile in enumerate(all_tiles):
                print(tile['value'], end=' ')
                if (i+1)%width == 0:
                    print()
            
            #-9,8,7

            for i, tile in enumerate(all_tiles):
                if (tile['value'] == "M"):
                    pos = pyautogui.locateAllOnScreen('Photos/dead.png', confidence = 0.98, grayscale=True)
                    print("Dead")
                    pos = sorted(pos, key=lambda x:(x[1], x[0]))
                    click(pos[0][0]+2, pos[0][1]+2)########################################################
                    pyautogui.moveTo(400, 685)
                    Dead = True

            if (Dead == True):
                break
            tbh = height*width
            if (len(all_tiles) != tbh):
                print("I AM HUNGRY FOR",tbh," BLOCKS. GIVE ME IT NOW")
                break
            
            flaggedblocks = []
            
            for i, tile in enumerate(all_tiles):
                if (type(tile['value']) == int ):
                    if (int(tile['value']) > 0):
                        nearblocks = check(i, all_tiles, width, height)
                        eblocks = []
                        for i, block in enumerate(nearblocks):
                            if (block['value'] == "_" or block['value'] == "F"):
                                eblocks.append(block)
                        if (len(eblocks) == int(tile['value'])):
                            for v, block in enumerate(eblocks):
                                if (block['value'] == "F" or block in flaggedblocks):
                                    pass
                                else:
                                    blockmove = True
                                    flaggedblocks.append(block)
                                    pyautogui.mouseDown(button='right', x = block['position'][0]+2, y = block['position'][1]+2)
                                    pyautogui.mouseUp(button='right')


            for blockk in flaggedblocks:
                blockk['value'] = "F"

                
            clicked_blocks = []

            for i, tile in enumerate(all_tiles):
                if (type(tile['value']) == int):
                    if (int(tile['value']) > 0):
                        flagged = []
                        nearblocks = check(i, all_tiles, width, height)
                        for v, block in enumerate(nearblocks):
                            if (block['value'] == "F"):
                                flagged.append(block)
                                nearblocks.remove(block)

                        if (len(flagged) == int(tile['value'])):
                            for v, block in enumerate(nearblocks):
                                if (block['value'] == "_" and not block in clicked_blocks):
                                    blockmove = True
                                    clicked_blocks.append(block)
                                    click(block['position'][0]+2,block['position'][1]+2)

            
            print(blockmove,guessing)
            WON2 = True
            for i, tile in enumerate(all_tiles):
                if (tile['value'] == "_"):
                    WON2 = False

            if (WON2 == True):
                WON = True
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("WON")
                print("Terminating Project!")
            if (WON2 == True):
                break
            
            if (guessing == True or blockmove == False):
                
                
                print("Guessing")
                guessingblocks = []
                for i, tile in enumerate(all_tiles):
                     if (tile['value'] == '_'):
                        guessingblocks.append(tile)
                choice = random.choice(guessingblocks)
                click(choice['position'][0]+2,choice['position'][1]+2)
                blockmove = True
                guessing = False

            


            print()
            print()
            print()
            print()
            pyautogui.moveTo(400, 685)
        if (WON == True):
            break

