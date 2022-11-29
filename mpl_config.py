from IPython.display import set_matplotlib_formats
set_matplotlib_formats('svg')
import matplotlib.pyplot as plt


latex = False
if latex:
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preambule'] = [r'\usepackage{amsmath}']
    plt.rcParams['text.latex.preambule'] = [r'\usepackage[utf8]{inputenc}']
    plt.rcParams['text.latex.preambule'] = [r'\usepackage[russian]{babel}']
    
    
plt.rcParams['figure.dpi'] = 500
    
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12
plt.rcParams['image.cmap'] = 'Set1'
plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['figure.constrained_layout.w_pad'] = 0
plt.rcParams['figure.constrained_layout.h_pad'] = 0


plt.rcParams['legend.loc'] = 'upper left'
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['figure.titleweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.frameon'] = True
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['lines.antialiased'] = True
plt.rcParams['lines.color'] = 'red'
plt.rcParams['svg.fonttype'] = 'none'


# plt.rcParams['']
# plt.rcParams['']
# plt.rcParams['']
def set_size(ratio=0.618):
    width = 15
    return (width, ratio*width)