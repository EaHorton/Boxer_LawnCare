from PIL import Image
import os

def generate_favicons(input_image_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the original image
    img = Image.open(input_image_path)

    # Define favicon sizes needed
    sizes = [
        (16, 16),
        (32, 32),
        (48, 48),
        (96, 96),
        (180, 180),  # Apple Touch Icon
        (192, 192),  # Android Chrome
        (512, 512),  # PWA icon
    ]

    # Generate favicon for each size
    for size in sizes:
        resized = img.resize(size, Image.Resampling.LANCZOS)
        if size == (16, 16):
            output_path = os.path.join(output_dir, 'favicon.ico')
        else:
            output_path = os.path.join(output_dir, f'favicon-{size[0]}x{size[1]}.png')
        resized.save(output_path)

    # Create webmanifest file
    manifest_content = {
        "name": "Boxer Lawn & Landscape",
        "short_name": "Boxer Lawn",
        "icons": [
            {
                "src": f"/favicon/favicon-192x192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": f"/favicon/favicon-512x512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ],
        "theme_color": "#ffffff",
        "background_color": "#ffffff",
        "display": "standalone"
    }

    import json
    with open(os.path.join(output_dir, 'site.webmanifest'), 'w') as f:
        json.dump(manifest_content, f, indent=2)

if __name__ == "__main__":
    input_image = "static/images/boxer-mascot.png"
    output_directory = "static/favicon"
    generate_favicons(input_image, output_directory)