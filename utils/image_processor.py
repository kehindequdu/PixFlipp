import io
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
from typing import Union, Tuple
import logging

from .filters import FILTERS, EFFECTS

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Handle image processing operations"""
    
    def __init__(self):
        self.max_size = (2048, 2048)  # Maximum image dimensions
    
    def _load_image(self, image_data: bytes) -> Image.Image:
        """Load image from bytes"""
        img = Image.open(io.BytesIO(image_data))
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'LA'):
            img = img.convert('RGB')
        return img
    
    def _save_image(self, image: Image.Image) -> bytes:
        """Save image to bytes"""
        output = io.BytesIO()
        image.save(output, format='PNG', optimize=True)
        return output.getvalue()
    
    def flip(self, image_data: bytes, mode: str) -> bytes:
        """Flip image horizontally, vertically, or both"""
        img = self._load_image(image_data)
        if mode == 'h':
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == 'v':
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        elif mode == 'b':
            img = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
        return self._save_image(img)
    
    def rotate(self, image_data: bytes, angle: int) -> bytes:
        """Rotate image by specified angle"""
        img = self._load_image(image_data)
        img = img.rotate(angle, expand=True, resample=Image.BICUBIC)
        return self._save_image(img)
    
    def apply_filter(self, image_data: bytes, filter_name: str) -> bytes:
        """Apply filter to image"""
        img = self._load_image(image_data)
        
        if filter_name in FILTERS:
            img = FILTERS[filter_name](img)
        else:
            logger.warning(f"Unknown filter: {filter_name}")
        
        return self._save_image(img)
    
    def apply_effect(self, image_data: bytes, effect_name: str) -> bytes:
        """Apply special effect to image"""
        img = self._load_image(image_data)
        
        if effect_name in EFFECTS:
            img = EFFECTS[effect_name](img)
        else:
            logger.warning(f"Unknown effect: {effect_name}")
        
        return self._save_image(img)
    
    def adjust_brightness(self, image_data: bytes, factor: float) -> bytes:
        """Adjust image brightness"""
        img = self._load_image(image_data)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(factor)
        return self._save_image(img)
    
    def adjust_contrast(self, image_data: bytes, factor: float) -> bytes:
        """Adjust image contrast"""
        img = self._load_image(image_data)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(factor)
        return self._save_image(img)
    
    def adjust_saturation(self, image_data: bytes, factor: float) -> bytes:
        """Adjust image saturation"""
        img = self._load_image(image_data)
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(factor)
        return self._save_image(img)
    
    def add_border(self, image_data: bytes, color: str = 'black', width: int = 20) -> bytes:
        """Add border to image"""
        img = self._load_image(image_data)
        img = ImageOps.expand(img, border=width, fill=color)
        return self._save_image(img)
    
    def resize(self, image_data: bytes, size: Tuple[int, int]) -> bytes:
        """Resize image"""
        img = self._load_image(image_data)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return self._save_image(img)
    
    def crop(self, image_data: bytes, box: Tuple[int, int, int, int]) -> bytes:
        """Crop image"""
        img = self._load_image(image_data)
        img = img.crop(box)
        return self._save_image(img)
