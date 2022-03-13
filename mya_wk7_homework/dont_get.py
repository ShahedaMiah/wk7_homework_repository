from tkinter import *
#importing the 'tkinter' module and using the wildcard(*) importing all classes/methods in the module

pronoun_options = ["he/him", "she/her", "they/the", "ve/ver", "xe/xem", "ze/zir"]
# created a 'pronoun_options' variable with a list of all the preferred pronoun options
drop = OptionMenu(root, clicked, *pronoun_options)
# create a 'drop' variable which uses the 'OptionMenu' method from the 'tkinker' module
# what is root????
drop.pick()