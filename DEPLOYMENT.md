# Deployment Guide

## Deploy Landing Page to Vercel

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm install -g vercel
   ```

2. **Deploy to Vercel**:
   ```bash
   vercel
   ```
   Follow the prompts to link your project.

3. **Or deploy via GitHub**:
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository `ledoit/Matrix-Maze`
   - Vercel will automatically detect and deploy the landing page

4. **Update landing page download links**:
   Once you have the Vercel URL, you can update the download buttons in `landing.html` with the actual download URLs.

## Build Downloadable App

### For macOS:
```bash
npm run tauri build
```
The built app will be in `src-tauri/target/release/bundle/macos/`

### For Windows:
```bash
npm run tauri build
```
The built app will be in `src-tauri/target/release/bundle/msi/` or `src-tauri/target/release/bundle/nsis/`

### For Linux:
```bash
npm run tauri build
```
The built app will be in `src-tauri/target/release/bundle/appimage/` or `src-tauri/target/release/bundle/deb/`

## Upload Builds

1. Create a `releases` folder in your repository or use GitHub Releases
2. Upload the built binaries to a hosting service (GitHub Releases, S3, etc.)
3. Update the download button links in `landing.html` with the actual URLs

## GitHub Releases (Recommended)

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Tag the version (e.g., `v1.0.0`)
4. Upload the built binaries for each platform
5. Copy the download URLs and update `landing.html`

