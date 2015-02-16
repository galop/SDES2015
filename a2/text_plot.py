import math

def downsample(arr, size):
    ''' Downsampler: samples array such that result is of length size
        arr: list/tuple
        size: int
    '''
    M = len(arr)
    hold = [arr[int(math.floor(M*i/size))] for i in range(size)]
    return hold
    
def offset(mat, HEIGHT, WIDTH):
    ''' adds offset to put plot in middle of screen
    '''
    hold = mat
    hold = [elem - min(hold) for elem in hold]
    hold = [elem * (HEIGHT/ (max(hold)-min(hold))) for elem in hold]
    return hold
        

def transform(x, y, HEIGHT, WIDTH):
    ''' scales the data to fill plot canvas
    '''
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)
    
#    if len(x) > WIDTH:      # downsample (feature disabled)
#        x = downsample(x, WIDTH)
#        y = downsample(y, WIDTH)
#    elif len(y) > HEIGHT:
#        y = downsample(y, HEIGHT)
#        x = downsample(x, HEIGHT)
    
    y = offset(y, HEIGHT, WIDTH) #remove offset and scale
        
    x_tr = map(int, x)  # Quantize in y-axis
    y_tr = map(int, y)  # Quantize in x-axis
    return (x_tr, y_tr)

def plot(x, y, HEIGHT=30, WIDTH=80):
    ''' Creates a text-based plot.
    
        x, y: int or float containers (list/tuple) with equal number of elements
        HEIGHT: height of plot canvas, values are scaled accordingly, default 30
        WIDTH: width of plot, first WIDTH number of points are plotted, default 80
    '''
    x_tr, y_tr = transform(x, y, HEIGHT, WIDTH)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (HEIGHT-1-i,j) in zip(y_tr, x_tr): #(0,0) is bottom left
                print '*',
            else:
                print ' ',
        print

def sineplot():
    H = 30
    W = 80
    x = range(W)
    y = [ math.sin(2*i*math.pi/W) for i in x]
    plot(x, y, H, W)

if __name__ == "__main__":
    sineplot()
