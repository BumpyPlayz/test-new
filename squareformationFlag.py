from mainprocessflag import LoadImages, process

side = input("Enter the side size: ")

if (side.isdigit):
    TILES = LoadImages()
    #startingprocess
    side = int(side)
    process(side,side,TILES)
