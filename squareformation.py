from mainprocess import LoadImages, process

side = input("Enter the side size: ")

if side.isdigit:
    TILES = LoadImages()
    # starting process
    side = int(side)
    process(side, side, TILES)
