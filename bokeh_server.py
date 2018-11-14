
from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox
from bokeh.models import ColumnDataSource, Slider, Select, Button, Toggle, CheckboxGroup, RadioGroup
from bokeh.plotting import figure
from numpy.random import random, normal, lognormal

#Initialize variables
N = 300
source = ColumnDataSource(data={'x':random(N), 'y':random(N)})

#Create plots and widgets
plot = figure()
circle_glyph = plot.circle(x='x', y='y', source=source)

slider = Slider(title='How many points?', start=100, end=1000, step=10, value=N)

menu = Select(options=['uniform','normal','lognormal'], value='uniform', title='Select distribution')

button = Button(label='Change color')

#Create callbacks
def slider_callback(attr, old, new):
    N = slider.value
    source.data = {'x':random(N), 'y':random(N)}
    
def menu_callback(attr, old, new):
    if    menu.value == 'uniform': f = random
    elif  menu.value == 'normal':  f = normal
    else:                          f = lognormal
    source.data={'x':f(size=N), 'y':f(size=N)}
    
def button_callback():
    circle_glyph.glyph.fill_color = 'firebrick'
    
slider.on_change('value', slider_callback)
menu.on_change('value', menu_callback)
button.on_click(button_callback)

layout = column(widgetbox(menu, slider, button), plot)

curdoc().add_root(layout)