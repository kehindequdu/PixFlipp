from PIL import Image, ImageFilter, ImageOps, ImageEnhance

def apply_blur(img):
    return img.filter(ImageFilter.GaussianBlur(radius=2))

def apply_sharpen(img):
    return img.filter(ImageFilter.SHARPEN)

def apply_contour(img):
    return img.filter(ImageFilter.CONTOUR)

def apply_emboss(img):
    return img.filter(ImageFilter.EMBOSS)

def apply_smooth(img):
    return img.filter(ImageFilter.SMOOTH_MORE)

def apply_detail(img):
    return img.filter(ImageFilter.DETAIL)

def apply_edge_enhance(img):
    return img.filter(ImageFilter.EDGE_ENHANCE_MORE)

def apply_find_edges(img):
    return img.filter(ImageFilter.FIND_EDGES)

# Effects
def apply_sepia(img):
    """Apply sepia tone effect"""
    img = img.convert('RGB')
    width, height = img.size
    pixels = img.load()
    
    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))
            
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            
            pixels[px, py] = (min(255, tr), min(255, tg), min(255, tb))
    
    return img

def apply_grayscale(img):
    """Convert to grayscale"""
    return img.convert('L').convert('RGB')

def apply_invert(img):
    """Invert colors"""
    return ImageOps.invert(img.convert('RGB'))

def apply_posterize(img):
    """Posterize image"""
    return ImageOps.posterize(img, bits=4)

def apply_solarize(img):
    """Solarize image"""
    return ImageOps.solarize(img, threshold=128)

def apply_equalize(img):
    """Equalize image histogram"""
    return ImageOps.equalize(img)

# Filter mapping
FILTERS = {
    'blur': apply_blur,
    'sharpen': apply_sharpen,
    'contour': apply_contour,
    'emboss': apply_emboss,
    'smooth': apply_smooth,
    'detail': apply_detail,
    'edge': apply_edge_enhance,
    'find_edges': apply_find_edges,
}

# Effect mapping
EFFECTS = {
    'sepia': apply_sepia,
    'grayscale': apply_grayscale,
    'invert': apply_invert,
    'posterize': apply_posterize,
    'solarize': apply_solarize,
    'equalize': apply_equalize,
}
