from ctypes.wintypes import SIZE
from turtle import *
import tkinter as TK
from random import randrange

#kaynak: https://www.geeksforgeeks.org/y-fractal-tree-in-python-using-turtle/

#eklenenler: rastgele renklerde dallar ve kullanıcıdan level ve size değerleri alma

speed('fastest')
  
# turning the turtle to face upwards
rt(-90)
  
# the acute angle between
# the base and branch of the Y
angle = 30
  
# function to plot a Y
                 
# tree of size 80 and level 7
#y(80, 7)

def user_input_size():
    print("Ağacın boyutu ne olsun? ")
    try:
        global sz
        sz = int(input()) 
    except ValueError:
        "Tam sayı gir beybi"
        user_input_size()
def user_input_level():
    print("Ağacın seviyesi ne olsun? ")
    try:
        global level
        level = int(input())
    except ValueError:
        "Tam sayı gir beybi"
        user_input_level()

def y(sz, level):   
  
    if level > 0:
        colormode(255)
          
        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        irand1 = randrange(1,255)
        irand2 = randrange(1,255)
        irand3 = randrange(1,255)
        pencolor(irand2, irand1//level, irand3)
          
        # drawing the base
        fd(sz)
  
        rt(angle)
  
        # recursive call for
        # the right subtree
        y(0.8 * sz, level-1)

        irand4 = randrange(1,255)
        irand5 = randrange(1,255)
        irand6 = randrange(1,255)  
        pencolor(irand4, irand5//level, irand6)
          
        lt( 2 * angle )
  
        # recursive call for
        # the left subtree
        y(0.8 * sz, level-1)

        irand7 = randrange(1,255)
        irand8 = randrange(1,255)
        irand9 = randrange(1,255)    
        pencolor(irand7, irand8//level, irand9)
          
        rt(angle)
        fd(-sz)
user_input_size()
user_input_level()
y(sz,level)

TK.mainloop()
