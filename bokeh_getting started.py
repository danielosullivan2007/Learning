# -*- coding: utf-8 -*-
"""
Created on Sat Sep 02 14:39:15 2017

@author: eardo
"""

from bokeh.plotting import figure
from bokeh.io import output_file, show

fg = figure()

x=3
y=[1,2,3,4]

fg.x(x,y)

output_file('sample_plot.html')
show(fg)