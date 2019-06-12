import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams
import os

here=os.path.abspath(__file__).replace("initiate.py","")

font_files = font_manager.findSystemFonts(fontpaths=[os.path.join(here, "./Brandon_Text")])
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)
plt.style.use(os.path.join(here, '1qbit.mplstyle'))


