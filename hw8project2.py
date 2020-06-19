#! hw8project1.py/usr/bin/python
# Exercise No.  14
# File Name:    hw8project2.py
# Programmer:   Arthur Utnehmer
# Date: April 6, 2020
#
# Problem Statement: (what you want the code to do)
# Write a program that converts a color image to grayscale.
# The user sup­ plies the name of a file containing a GIF or PPM image, and
# the program loads the image and displays the file. At the click of the mouse, the pro­ gram converts the image to grayscale.
# The user is then prompted for a file name to store the grayscale image in.
# You will probably want to go back and review the Image object from the graphics libarary (Section 4.8.4) .
# The basic idea for converting the image is to go through it pixel by pixel and convert each one from color to an appropriate shade of gray.
# A gray pixel is created by setting its red, green, and blue components to have the same brightness. So color_rgb(0, 0, 0) is black, color_rgb(255, 255, 255) is white, and
# color_rgb( 127, 127, 127) is a gray "halfway'' between. You should use a weighted average of the original RGB values to determine the brightness of the gray.
# Here is the pseudocode for the grayscale algorithm:
#   for each row in the image:
#       for each col11mn in the image :
#           r, g, b = get pixel information for current row and column brightness = int(round(0.299r + 0.587g + 0.114b))
#           set pixel to color_rgb(brightness, brightness, brightness)
#       update the image # to see progress row by row
# Note: The pixel operations in the Image class are rather slow, so you will want to use relatively small images (not 12 megapixels) to test your program.
#
# Overall Plan (step-by-step,howyou want the code to make it happen):
# 1.First generate a window with a text prompt asking for the file name where the image is contained.
# 2.Display image after the user has entered the location as well as the name of the file.
# 3.After mouse is clicked, convert the image to grayscale.
# 4.After the image is converted, save the image to a file name that the user specifies.

# import necessary python libraries
from graphics import *

# Create main functiond

def main():

    #Draw window that will prompt for the file name
    nameOfFile = ""
    win = GraphWin("GrayScale Image Converter" , 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    #Ask for the file name and get the text.
    Text(Point(1.5,3) , "Enter the name of the file that contains the \n image you wish to convert to grayscale: ").draw(win).setSize(20)
    Text(Point(1.5,1.5) , "Lets Play").draw(win)
    inputText = Entry(Point (1.5 , 2) , 20)
    inputText.setText ("Enter File Name here.")
    inputText.draw (win)
    win.getMouse()

    #Next display the image with the file name.
    fileName = inputText.getText()
    if(fileName == "Enter File Name here."):
        {
        sys.exit()
        }
    win.close()
    centerPointWidth = Image(Point(0,0), fileName).getWidth()
    centerPointHeight = Image(Point(0,0), fileName).getHeight()
    userImage = Image(Point(centerPointWidth/2,centerPointHeight/2), fileName)
    win = GraphWin(fileName, centerPointWidth, centerPointHeight)
    userImage.draw(win)

    #Confirm the user wants a conversion and start.
    Text(Point(centerPointWidth/2,centerPointHeight/2) , "Click here to confirm the conversion. ").draw(win).setTextColor("red")
    win.getMouse()
    grayScaleConvesion(inputText.getText (), win, userImage)


def saveToFile(Image,win):
    #Create window dialogue.
    Text(Point(Image.getWidth()/2,Image.getHeight()/2) , "Please enter the name of the file you want the image named than click here.").draw(win).setTextColor("red")
    inputText = Entry(Point(Image.getWidth()/2,Image.getHeight()/3) , 20)
    inputText.setText ("Enter file name here.")
    inputText.draw (win)
    win.getMouse()
    #Save to file
    Image.save(inputText.getText())

def grayScaleConvesion(fileName, win, userImage):
    #Do the conversion.
    for x in range(0, userImage.getWidth()):
        for y in range(0, userImage.getHeight()):
            r, g, b = userImage.getPixel(x, y)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            userImage.setPixel (x , y , (color_rgb(brightness, brightness, brightness)))
        userImage.undraw()
        userImage.draw(win)


    saveToFile(userImage, win)
    win.close()

main()


