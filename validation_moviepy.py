import sys
import numpy as np

def test_moviepy_modernization():
    print("--- Starting MoviePy v2.2.0 + NumPy 2.x Verification ---")
    
    try:
        # V2.X IMPORT STYLE: moviepy.editor is now just moviepy
        from moviepy import ColorClip
        print("--> MoviePy v2.x modules imported successfully.")

        # 1. Create a simple clip
        print("--> Generating synthetic 640x480 clip...")
        clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=1)
        
        # 2. TRIGGER THE NUMPY 2.X TRAP
        # MoviePy internally uses array transformations. 
        # NumPy 2.x removed 'np.float' (now just float). 
        # This will trigger an AttributeError if Pip installs NumPy 2.x.
        print(f"--> Testing frame processing with NumPy {np.__version__}...")
        
        # We manually use the deprecated alias to see if the environment supports it
        # This simulates a legacy internal call inside the MoviePy source.
        legacy_type = np.float 
        frame = clip.get_frame(0).astype(legacy_type)
        
        if frame.shape == (480, 640, 3):
            print(f"    [✓] Frame processed. Mean value: {np.mean(frame):.2f}")
        else:
            raise ValueError("Unexpected frame dimensions.")

        print("--- SMOKE TEST PASSED ---")

    except ModuleNotFoundError as e:
        print(f"CRITICAL FAILURE: {str(e)}")
        print("HINT: MoviePy 2.0+ removed 'moviepy.editor'. Use 'from moviepy' instead.")
        sys.exit(1)
    except AttributeError as ae:
        print(f"CRITICAL VALIDATION FAILURE: {str(ae)}")
        # This is where AURA wins (detecting np.float removal)
        sys.exit(1)
    except Exception as e:
        print(f"UNEXPECTED FAILURE: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_moviepy_modernization()