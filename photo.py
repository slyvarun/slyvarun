from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

# ==========================================
# CONFIGURATION
# ==========================================
INPUT_IMAGE = '1111.png'       # <-- Your static image
OUTPUT_GIF = 'varun_binary.gif'   # The final animated output
COLUMNS = 120                     # Detail level (higher = more text)
FRAMES = 40                       # Number of frames (higher = longer loop, larger file)
SPEED = 80                        # Speed of the scroll (ms per frame)
# ==========================================

def get_font():
    try:
        # Use a monospaced font so the columns align perfectly
        return ImageFont.truetype("consola.ttf", 10) 
    except IOError:
        return ImageFont.load_default()

def process_image():
    print(f"Loading {INPUT_IMAGE}...")
    try:
        img = Image.open(INPUT_IMAGE).convert("RGB")
    except FileNotFoundError:
        print(f"Error: Could not find {INPUT_IMAGE}. Please check the filename.")
        return
        
    font = get_font()
    
    # Calculate dimensions to maintain aspect ratio
    w, h = img.size
    aspect_ratio = h / w
    
    char_w = 6
    char_h = 10
    
    grid_w = COLUMNS
    grid_h = int(aspect_ratio * COLUMNS * (char_w / char_h))
    
    out_w = grid_w * char_w
    out_h = grid_h * char_h

    # Resize the original image to our grid size so we can sample the exact colors
    resized_img = img.resize((grid_w, grid_h))
    pixels = np.array(resized_img)

    # Initialize a 2D list of random 0s and 1s for the starting grid
    char_grid = [['1' if random.random() > 0.5 else '0' for _ in range(grid_w)] for _ in range(grid_h)]
    
    matrix_frames = []

    print("Rendering horizontal data stream...")
    for frame_num in range(FRAMES):
        # Create a blank black canvas for this frame
        new_frame = Image.new('RGB', (out_w, out_h), color=(0, 0, 0))
        draw = ImageDraw.Draw(new_frame)
        
        for y in range(grid_h):
            # THE MAGIC: Shift the row to the right by removing the last character 
            # and inserting a new random binary number at the very beginning (left side)
            char_grid[y].pop()
            char_grid[y].insert(0, random.choice(['0', '1']))
            
            for x in range(grid_w):
                char = char_grid[y][x]
                
                # Get the RGB color from your original photo at this exact spot
                r, g, b = pixels[y, x]
                
                # Draw the scrolling binary number using your photo's color
                draw.text((x * char_w, y * char_h), char, font=font, fill=(r, g, b))
                
        matrix_frames.append(new_frame)
        print(f"Rendered frame {frame_num + 1}/{FRAMES}")

    print(f"Compiling GIF... saving to {OUTPUT_GIF}")
    matrix_frames[0].save(
        OUTPUT_GIF,
        save_all=True,
        append_images=matrix_frames[1:],
        optimize=True,
        duration=SPEED,
        loop=0
    )
    print("Success! Your binary portrait is ready.")

if __name__ == "__main__":
    process_image()