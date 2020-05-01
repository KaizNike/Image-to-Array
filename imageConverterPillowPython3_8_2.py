from PIL import Image
import numpy as nm
# To Add: Image resizing in order to get a proper image

def get_image(image_path, tilex, tiley, tileOne):
    """get a numpy array of an image so that one can access values [x][y]."""
    image = Image.open(image_path, 'r')
    width, height = image.size
    tileswide = int(round( width / tilex, 0))
    tilestall = int(round(height / tiley, 0))
    middlex = int(round(tilex / 2, 0) + 1)
    middley = int(round(tiley / 2, 0) + 1)
    print('Tiles: ' + '(' + str(tileswide) + ', ' + str(tilestall) + ')')
    print('Tile Middle: ' + '(' + str(middlex) + ', ' + str(middley) + ')')
    pixel_values = list(image.getdata())
    w, h = tileswide, tilestall;
    finalArray = [[0 for x in range(w)] for y in range(h)]
    #finalArray = nm.zeros((tileswide, tilestall))
    for y in range(0, tilestall):
        for x in range(0, tileswide):      
            currentX = (middlex * (x+1))
            currentY = (middley * (y+1))
            look = pixel_values[width*currentY+currentX]
            if look == tileOne:
                finalArray[y][x] = 0
            else:
                finalArray[y][x] = 1
    print(finalArray)
    if image.mode == 'RGB':
        channels = 3
    elif image.mode == 'L':
        channels = 1
    elif image.mode == 'RGBA':
        channels = 4
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    #pixel_values = nm.array(pixel_values).reshape((width, height, channels))
    #return pixel_values
    return finalArray


def document_write(file_path, file_data):
    f = open(file_path, 'w')
    f.write("Pixels RGBA : %s\n" % file_data)
    f.close()

def image_write(file_path, file_data):
    y = len(file_data)
    x = len(file_data[0])
    img = Image.new('RGB', (x, y), color = 'white')
    pixels = img.load() #creates the pixel map
    width, height = img.size
    print(pixels[0,0])
    for i in range(width):
        for j in range(height):
            if file_data[j][i] == 0:
                pixels[i, j] = tileWaterRGB
            else:
                pixels[i, j] = tileGrassRGB
    #img.show()
    img.save(file_path)
    return
    
tileGrassRGB = (124, 252, 0)    #lawn green
tileWaterRGB = (23, 8, 37)  #dark navy blue
setX = 5    #a tile's x width
setY = 9    #a tile's y height
inputImage = 'worldsmall.jpg'   #change to name of image needed
#show_image = get_image('theworld.jpg')
#show_image = get_image('testing.png')
# tilex and tiley must be odd numbers as of now
#show_image = get_image('worldsmall.jpg', 65, 65, tileWaterRGB)
#show_image = get_image('worldsmall.jpg', 5, 5, tileWaterRGB)
show_image = get_image(inputImage, setX, setY, tileWaterRGB)
print("Start writing.")
image_write('output.png', show_image)
document_write("output.txt", show_image)
print("Done!")
#print(show_image)
wait = input()
