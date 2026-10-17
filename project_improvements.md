# Recommended Improvements for a Stronger CBSE Project

These improvements are still suitable for a school-level project and make the system more polished without making it too complex.

## Suggested Features
- Undo/Redo option (keyboard: `z` undo, `y` redo)
- Clear canvas (keyboard: `x`)
- Brush size control (`+` / `-`)
- Color selection presets (keys `1`–`5`)
- Save the drawing as PNG (`s`) into `saved/` folder
- Better gesture detection with frame-debounce and smoothing
- On-screen overlays showing current mode, brush size, color, and shortcuts

## Why These Features Help
These additions make the project more interactive, easier to demonstrate, and more impressive during practical evaluation.

## Best Practical Upgrades
1. Undo/redo using a stored list of canvas states (implemented)
2. Clear canvas for easier reset (implemented)
3. Save drawing as an image file in the `saved/` folder (implemented)
4. Brush size adjustment with keyboard commands (`+` / `-`) (implemented)
5. Better on-screen overlays and status updates (implemented)

Demo controls (keyboard + gesture):
- Draw: raise index finger alone for 3 frames
- Erase: raise index + middle fingers for 3 frames
- Undo: press `z`
- Redo: press `y`
- Clear: press `x`
- Save image: press `s` (file saved to `saved/`)
- Change brush size: `+` / `-`
- Change color: press `1`..`5` for presets
- Blackboard mode: press `b` to toggle a plain blackboard background; a fingertip pointer shows the hand location

## Result
These changes keep the project educational and manageable while making it much stronger for demonstration and viva.
