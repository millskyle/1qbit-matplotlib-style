import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams
import os
import matplotlib

here=os.path.abspath(__file__).replace("initiate.py","")

font_files = font_manager.findSystemFonts(fontpaths=[os.path.join(here, "./Brandon_Text")])
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)
plt.style.use(os.path.join(here, '1qbit.mplstyle'))

#override the harsh RGB colors with more aesthetic ones:
newc = dict(
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


