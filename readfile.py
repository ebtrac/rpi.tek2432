#!/bin/python3

from gpibPrintFunctions import TekPlotSaver

saver = TekPlotSaver(0,1)

filename = input("filename?")

print("Press PLOT on the Tektronix 2432... <any key to continue>")
input()

print("reading data to", filename)

saver.write_data_to_file(filename)

print("Done")

