import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams
import os
import matplotlib
import numpy as np


here=os.path.abspath(__file__).replace("initiate.py","")

#If we could distribute the font, then this would use it, but we cannot distribute it, so
#these following three lines don't actually do anything.
font_files = font_manager.findSystemFonts(fontpaths=[os.path.join(here, "./Brandon_Text")])
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

plt.style.use(os.path.join(here, '1qbit.mplstyle'))

#override the harsh RGB colors with more aesthetic ones:
newc = dict(
        r="#CF5C5E",
        b="#5C97CF",
        g="#5ECF5C",
        red="#CF5C5E",
        blue="#5C97CF",
        green="#5ECF5C",
        orange="#E69A45",
        yellow="#E6D645",
        magenta="#CE5CCF",
        fucshia="#CF5CCA",
        purple="#945CCF",
        violet="#5C5ECF",
        darkblue="#3352AD",
        cyan="#5CCFCE",
)

for key in newc.keys():
    matplotlib.colors.ColorConverter.colors[key] = newc[key]


#Add a better "flag" colormap:
flag5 = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "blue", "C4"]*5 )
flag10 = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "blue", "C4"]*10 )
flag25 = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white", "blue", "C4"]*25 )
plt.register_cmap('1qbit25', flag25)
plt.register_cmap('1qbit10', flag10)
plt.register_cmap('1qbit5', flag5)


