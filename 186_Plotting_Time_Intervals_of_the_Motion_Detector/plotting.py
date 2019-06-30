from motion_detector import df
from bokeh.plotting import figure, output_file, show

plot = figure(width=600, height=400)

plot.title.text="Motion graph"

q = plot.quad(left=df["Start"], right=df["End"], top=1, bottom=0, color="green")

output_file("Motion_graph.html")
show(plot)
