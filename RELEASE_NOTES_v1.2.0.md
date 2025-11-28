# Matrix Maze v1.2.0

## Major Update: 5-Level System

Matrix Maze now features a complete 5-level progression system with increasing difficulty and color-coded themes!

### New Features

**5-Level Progression System**
- Navigate through 5 progressively challenging levels
- Maze sizes increase from 8×8 (Level 1) to 12×12 (Level 5)
- Each level features a unique color theme:
  - **Level 1**: Green
  - **Level 2**: Pink/Magenta
  - **Level 3**: Red
  - **Level 4**: Purple
  - **Level 5**: Blue

**Personal Best Tracking**
- Track your best time for each individual level
- Compete for the best total time across all 5 levels
- "PERSONAL BEST!" notifications when you set new records
- Persistent best times saved between sessions

**Enhanced Win Screen**
- Detailed completion statistics for each level
- Total time and best total time display
- Level-by-level breakdown of your run
- Beautiful ASCII art "LEVEL COMPLETE!" message

**Improved Gameplay**
- Randomized starting positions (no more always spawning in the corner!)
- Randomized exit positions for varied gameplay
- "FIND THE EXIT!" flashing message at level start
- Improved maze generation with better randomization

**Visual Improvements**
- New pixel art icon featuring the running figure in the maze
- Dynamic color theming that matches each level
- Improved controls display with level-specific colors
- Better visual feedback throughout the game

### Controls

- **WASD**: Move (W/S forward/backward, A/D strafe)
- **Q/E**: Turn left/right
- **SPACE**: Next Level/Play Again (after win)

### Installation

**macOS Users**: If you see "app is damaged" after installation, right-click the app and select "Open", or run this in Terminal:
```bash
xattr -cr /Applications/Matrix\ Maze.app
```

### Bug Fixes

- Fixed total time calculation to show actual run times
- Improved maze generation seed randomization
- Fixed exit position randomization edge cases

### Technical Improvements

- Centralized color system for easy theme customization
- Improved state management for multi-level progression
- Better file handling for best times persistence

---

**Download**: [Matrix Maze_1.2.0_aarch64.dmg](https://github.com/ledoit/Matrix-Maze/releases/download/v1.2.0/Matrix%20Maze_1.2.0_aarch64.dmg)

**Full Changelog**: See [commit history](https://github.com/ledoit/Matrix-Maze/compare/v1.1.0...v1.2.0)

