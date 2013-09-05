# from https://gist.github.com/olooney/1601455 cuz i 
# hate rewriting this function all the time
from PIL import Image
from cStringIO import StringIO
 
def flat( *nums ):
  'Build a tuple of ints from float or integer arguments. Useful because PIL crop and resize require integer points.'
  
  return tuple( int(round(n)) for n in nums )
 
class Size(object):
  def __init__(self, pair):
    self.width = float(pair[0])
    self.height = float(pair[1])
 
  @property
  def aspect_ratio(self):
    return self.width / self.height
 
  @property
  def size(self):
    return flat(self.width, self.height)
 
def cropped_thumbnail(img, size):
  '''
  Builds a thumbnail by cropping out a maximal region from the center of the original with
  the same aspect ratio as the target size, and then resizing. The result is a thumbnail which is
  always EXACTLY the requested size and with no aspect ratio distortion (although two edges, either
  top/bottom or left/right depending whether the image is too tall or too wide, may be trimmed off.)
  '''
  
  original = Size(img.size)
  target = Size(size)
 
  if target.aspect_ratio > original.aspect_ratio:
    # image is too tall: take some off the top and bottom
    scale_factor = target.width / original.width
    crop_size = Size( (original.width, target.height / scale_factor) )
    top_cut_line = (original.height - crop_size.height) / 2
    img = img.crop( flat(0, top_cut_line, crop_size.width, top_cut_line + crop_size.height) )
  elif target.aspect_ratio < original.aspect_ratio:
    # image is too wide: take some off the sides
    scale_factor = target.height / original.height
    crop_size = Size( (target.width/scale_factor, original.height) )
    side_cut_line = (original.width - crop_size.width) / 2
    img = img.crop( flat(side_cut_line, 0,  side_cut_line + crop_size.width, crop_size.height) )
    
  return img.resize(target.size, Image.ANTIALIAS)

def thumbnail(data, size=(150,150)):
  image = Image.open(StringIO(data))
  thumbio = StringIO()
  thumb_image =  cropped_thumbnail(image, size)
  thumb_image.save(thumbio, format="JPEG")
  return thumbio.getvalue()

