from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d, %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d, %H:%M:%S")

cds = ColumnDataSource(df)


plot = figure(x_axis_type="datetime", width=600, height=400)

plot.title.text="Motion graph"

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
plot.add_tools(hover)


q = plot.quad(left="Start", right="End", top=1, bottom=0, color="green", source=cds)

output_file("Motion_graph.html")
show(plot)
