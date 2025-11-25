#!/usr/bin/env python3
"""
Create Matrix Maze icon
Install Pillow first: pip3 install Pillow
"""

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Please install Pillow: pip3 install Pillow")
    exit(1)

import os

# Create icon directory
os.makedirs('icons', exist_ok=True)

# Create a 512x512 icon (Tauri will use this)
size = 512
img = Image.new('RGBA', (size, size), (0, 0, 0, 255))
draw = ImageDraw.Draw(img)

# Draw maze-themed icon
border = size // 8
cell_size = (size - 2 * border) // 4

# Outer border (green)
draw.rectangle([border, border, size - border, size - border], 
               outline=(0, 255, 0, 255), width=8)

# Draw maze cells
for i in range(4):
    for j in range(4):
        x = border + i * cell_size
        y = border + j * cell_size
        
        # Create maze pattern
        if (i + j) % 3 != 0:
            draw.rectangle([x, y, x + cell_size, y + cell_size], 
                         fill=(0, 255, 0, 80), outline=(0, 255, 0, 255))

# Draw path (solution)
path_width = 16
start_x = border + cell_size // 2
start_y = border + cell_size // 2
end_x = size - border - cell_size // 2
end_y = size - border - cell_size // 2

# Path from start to end
draw.line([start_x, start_y, start_x, start_y + cell_size * 2], 
          fill=(0, 255, 0, 255), width=path_width)
draw.line([start_x, start_y + cell_size * 2, end_x, start_y + cell_size * 2], 
          fill=(0, 255, 0, 255), width=path_width)
draw.line([end_x, start_y + cell_size * 2, end_x, end_y], 
          fill=(0, 255, 0, 255), width=path_width)

# Save
img.save('icons/icon.png')
print(f'Created icons/icon.png ({size}x{size})')

