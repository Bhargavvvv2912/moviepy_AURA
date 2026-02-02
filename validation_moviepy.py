import sys
import numpy as np
from moviepy.editor import ColorClip

def test_numpy_compatibility():
    print("--- Starting MoviePy + NumPy 2.x Verification ---")
    
    try:
        # 1. Create a simple clip
        # moviepy internally converts frames to numpy arrays
        print("--> Generating synthetic 640x480 clip...")
        clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=1)
        
        # 2. Trigger Array Processing
        # Many video effects in MoviePy use np.float or np.empty with old types
        print("--> Applying a simple brightness effect (Array Transformation)...")
        dark_clip = clip.fl_image(lambda image: (image * 0.5).astype(np.uint8))
        
        # 3. Execution Check
        frame = dark_clip.get_frame(0)
        
        if frame.shape == (480, 640, 3):
            print(f"    [✓] Frame processed successfully with NumPy {np.__version__}")
        else:
            raise ValueError("Unexpected frame dimensions.")

        print("--- SMOKE TEST PASSED ---")

    except AttributeError as ae:
        print(f"CRITICAL VALIDATION FAILURE: {str(ae)}")
        # Likely: "module 'numpy' has no attribute 'float'" or similar
        sys.exit(1)
    except Exception as e:
        print(f"UNEXPECTED FAILURE: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_numpy_compatibility()