from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

# ==========================================
# CONFIGURATION
# ==========================================
INPUT_GIF = 'miles-morales-swing.gif'        # <-- Change this to your downloaded GIF name
OUTPUT_GIF = 'spiderman_matrix.gif' # The final GitHub animation
COLUMNS = 100                      # Detail level (higher = more text, larger file size)
THRESHOLD = 30                     # Minimum brightness to draw a character (0-255)
# ==========================================

def get_font():
    # Load a monospaced font so the columns align perfectly
    try:
        # Windows: 'consola.ttf', Mac: 'Menlo.ttc', Linux: 'DejaVuSansMono.ttf'
        return ImageFont.truetype("consola.ttf", 10) 
    except IOError:
        return ImageFont.load_default()

def process_gif():
    print(f"Loading {INPUT_GIF}...")
    
    # 1. Open the original GIF and extract all frames
    gif = Image.open(INPUT_GIF)
    original_frames = []
    
    try:
        while True:
            # Convert to RGB to ensure consistent color processing
            original_frames.append(gif.convert("RGB"))
            gif.seek(len(original_frames))
    except EOFError:
        pass # End of GIF frames
        
    print(f"Extracted {len(original_frames)} frames. Initializing Matrix engine...")
    
    font = get_font()
    matrix_frames = []
    
    # Calculate dimensions based on the first frame
    w, h = original_frames[0].size
    aspect_ratio = h / w
    
    # Character block dimensions
    char_w = 6
    char_h = 10
    
    # Grid dimensions
    grid_w = COLUMNS
    grid_h = int(aspect_ratio * COLUMNS * (char_w / char_h))
    
    # Final output dimensions
    out_w = grid_w * char_w
    out_h = grid_h * char_h

    # 2. Process each frame
    for i, frame in enumerate(original_frames):
        # Convert to grayscale and resize to our grid map
        gray_frame = frame.convert("L").resize((grid_w, grid_h))
        gray_pixels = np.array(gray_frame)
        
        # Create a new blank black canvas
        new_frame = Image.new('RGB', (out_w, out_h), color=(0, 0, 0))
        draw = ImageDraw.Draw(new_frame)
        
        # Map pixels to binary
        for y in range(grid_h):
            for x in range(grid_w):
                intensity = gray_pixels[y, x]
                
                # Skip dark background pixels to maintain the silhouette
                if intensity < THRESHOLD:
                    continue
                
                char = random.choice(['0', '1'])
                
                # Color logic: Darker pixels are dark green, bright pixels glow white-green
                g = max(50, intensity)
                r = max(0, intensity - 100)
                b = max(0, intensity - 100)
                
                # Draw the binary character
                draw.text((x * char_w, y * char_h), char, font=font, fill=(r, g, b))
                
        matrix_frames.append(new_frame)
        print(f"Rendered frame {i + 1}/{len(original_frames)}")

    # 3. Save the new animated GIF
    print(f"Compiling Matrix GIF... saving to {OUTPUT_GIF}")
    matrix_frames[0].save(
        OUTPUT_GIF,
        save_all=True,
        append_images=matrix_frames[1:],
        optimize=True,
        duration=gif.info.get('duration', 80), # Use original GIF speed
        loop=0 # Infinite loop
    )
    print("Success! System output complete.")

if __name__ == "__main__":
    process_gif()