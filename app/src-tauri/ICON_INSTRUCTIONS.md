# Creating an Icon for Matrix Maze

## Option 1: Use Tauri's Icon Generator (Recommended)

1. Create or download a 1024x1024 PNG image with your icon design
2. Save it as `app-icon.png` in the `app/` directory
3. Run:
   ```bash
   cd app
   npm run tauri icon app-icon.png
   ```
   This will automatically generate all required icon sizes for macOS, Windows, and Linux.

## Option 2: Manual Icon Creation

You can create icons using:
- **Online tools**: [Favicon.io](https://favicon.io), [IconKitchen](https://icon.kitchen)
- **Design software**: Figma, Photoshop, GIMP
- **AI generators**: DALL-E, Midjourney (create a maze-themed icon)

The icon should be:
- Square (1024x1024 recommended)
- PNG format with transparency
- Maze/Matrix themed to match your game

## Current Icon

The current `icons/icon.png` is a placeholder. Replace it with your custom icon using Option 1 above.

