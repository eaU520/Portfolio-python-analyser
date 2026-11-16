#Not available in VSCodroid
<<<<<<< HEAD
"""import matplotlib.pyplot as plotter
def simple_plot():
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    plotter.plot(x,y)
    plotter.show()
"""
=======
import matplotlib.pyplot as plotter
def simple_plot(x,x_label, y, y_label, title):
    plotter.plot(x,y)
    plotter.xlabel(x_label)
    plotter.ylabel(y_label)
    plotter.title(title)
    plotter.savefig("./reports/volt_time_plot.png")
    plotter.legend(y_label)#Is an array of each line that is plotted    plotter.savefig("reports/volt_time_plot.png")
    plotter.show()
>>>>>>> 06db51ca5f80c44a5417b08ec030f677111664ac
