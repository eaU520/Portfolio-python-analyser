#Not available in VSCodroid
import matplotlib.pyplot as plotter
def simple_plot(x,x_label, y, y_label, title):
    plotter.plot(x,ygit)
    plotter.xlabel(x_label)
    plotter.ylabel(y_label)
    plotter.title(title)
    plotter.savefig("./reports/volt_time_plot.png")
    plotter.legend(y_label)#Is an array of each line that is plotted    plotter.savefig("reports/volt_time_plot.png")
    plotter.show()