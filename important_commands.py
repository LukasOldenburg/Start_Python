import py_paradigms as para
import os
import numpy as np

# input window
# Name = input('Wie heißt du?')
# print('Hallo ' + Name)

# range/length
A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
custom_range = range(4, 10, 2)  # Start, Ende-1, Schrittweite
for n in custom_range:
    print(A[n])

# open/close/write in editor-files
open_testfile1 = open('Testfile1.txt', 'r+')  # r=read, w=write, a=append (add), r+=read and write
lines2array = open_testfile1.readlines()
open_testfile1.write('\nadded line')  # \n new line
print(lines2array[2])
open_testfile1.close()

# Arbeitsverzeichnis finden/überschreiben
print(os.getcwd())

# Import/install Modules
# import intern modules/functions
# import file ist am Anfang!
print(para.multiplikation2numbers([2, 200]))

# import external modules
# built in: External Librariers - Python - Lib
# install Module - cmd -> pip install 'modulename'
# deinstall Module - cmd -> pip deinstall 'modulname'

NumpyArray = np.array([[1, 2, 3], [1, 2, 3]])
print(NumpyArray)

