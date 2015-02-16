import text_plot

try:
    text_plot.plot(range(25), range(25))
except ValueError:
    print "Values are wrong."

try:
    text_plot.plot(range(25), range(25), 40, 40)
except IndexError:
    print "Plot dimensions are not correct."

try:
    text_plot.plot(range(80), [-20.0 + i for i in range(80)])
except ValueError:
    print "Floating point or negative value error"
    
try:
    text_plot.plot(range(25), range(-25))
except ValueError:
    print "Plot dimensions must be positive integers"
    
try:
    x = range(100)
    y = [0.01*i*i for i in x]
    text_plot.plot(x,y)
except (ValueError, IndexError):
    print "Error occurred"
    
