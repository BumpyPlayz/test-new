from mainprocess import LoadImages, process

height = input("Enter height of the grid: ")
width = input("Enter width of the grid: ")

if (height.isdigit and width.isdigit()):
    TILES = LoadImages()
    #startingprocess
    height = int(height)
    width = int(width)
    process(height,width,TILES)
