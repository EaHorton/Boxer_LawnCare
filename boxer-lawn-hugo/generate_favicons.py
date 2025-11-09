#!/usr/bin/env python3
"""
Generate favicon files from boxer-mascot.png
"""
from PIL import Image
import os

# Source image path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_IMAGE = os.path.join(SCRIPT_DIR, 'static', 'images', 'boxer-mascot.png')
FAVICON_DIR = os.path.join(SCRIPT_DIR, 'static', 'favicon')

# Ensure favicon directory exists
os.makedirs(FAVICON_DIR, exist_ok=True)

def create_favicon(size, output_name):
    """Create a favicon of specified size"""
    with Image.open(SOURCE_IMAGE) as img:
        # Convert to RGBA if not already
        img = img.convert('RGBA')
        
        # Create a square image with padding
        desired_size = max(img.size)
        new_img = Image.new('RGBA', (desired_size, desired_size), (255, 255, 255, 0))
        
        # Calculate position to paste original image
        x = (desired_size - img.size[0]) // 2
        y = (desired_size - img.size[1]) // 2
        new_img.paste(img, (x, y))
        
        # Resize to target size
        resized = new_img.resize((size, size), Image.Resampling.LANCZOS)
        
        # Save the image
        output_path = os.path.join(FAVICON_DIR, output_name)
        resized.save(output_path, optimize=True)
        print(f"Created {output_name}")

def create_webmanifest():
    """Create site.webmanifest file"""
    manifest = {
        "name": "Boxer Lawn & Landscape",
        "short_name": "Boxer Lawn",
        "icons": [
            {
                "src": "/favicon/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/favicon/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "theme_color": "#8B0000",
        "background_color": "#ffffff",
        "display": "standalone"
    }
    
    import json
    manifest_path = os.path.join(FAVICON_DIR, 'site.webmanifest')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print("Created site.webmanifest")

def main():
    # Create various sizes
    create_favicon(16, 'favicon-16x16.png')
    create_favicon(32, 'favicon-32x32.png')
    create_favicon(180, 'apple-touch-icon.png')
    create_favicon(192, 'android-chrome-192x192.png')
    create_favicon(512, 'android-chrome-512x512.png')
    
    # Create webmanifest
    create_webmanifest()
    
    print("\nFavicon generation complete!")

if __name__ == '__main__':
    main()