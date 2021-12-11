



















# import pyformulas as pf
# import matplotlib.pyplot as plt
# import numpy as np
# import time

# def drawRealTimeLinePlot(x, y):
#     fig = plt.figure()

#     # Plot params:
#     x_range = range(len(x))

#     screen = pf.screen(title='Plot')

#     start = time.time()

#     for i in x_range:
#         t = time.time() - start

#         current_x = np.linspace(t-3, t, 1)
#         current_y = y[i]
#         plt.xlim(t-3,t)
#         plt.ylim(0, y[i] + 5)
#         plt.plot(current_x, current_y, c='black')

#         # If we haven't already shown or saved the plot, then we need to draw the figure first...
#         fig.canvas.draw()

#         image = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
#         image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

#         screen.update(image)