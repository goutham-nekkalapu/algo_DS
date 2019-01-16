

"""
this is a func to rescale a given image to new dimensions 
using the 'nearest neighbour' method.
"""

def nearestNeighborScaling( source, newWid, newHt ):
    """
    note that here, the scale ratio :(float(width/newWid))
    can be cal before hand, instead of cal each time 
    """
    target = makeEmptyPicture(newWid, newHt)
    width = getWidth( source )
    height = getHeight( source )
    for x in range(0, newWid):  
      for y in range(0, newHt):
        srcX = int( round( float(x) / float(newWid) * float(width) ) ) # can be modif to int(round(float (x*scale_ratio)))
        srcY = int( round( float(y) / float(newHt) * float(height) ) )
        srcX = min( srcX, width-1)
        srcY = min( srcY, height-1)
        tarPix = getPixel(target, x, y )
        srcColor = getColor( getPixel(source, srcX, srcY) )
        setColor( tarPix, srcColor)

    return target
