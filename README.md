### Simple Motion Detection using OpenCV

This Python script `detect_mtion.py` provides a basic implementation of a motion detection system using the OpenCV library. It captures video from a webcam and identifies moving objects by comparing consecutive frames. When motion is detected, it draws a green rectangle around the moving area.

#### How it Works

The script follows these steps to detect motion:

1.  **Camera Initialization:** It starts by accessing the computer's webcam using `cv2.VideoCapture(0)`.
2.  **Initial Frame Capture:** The first frame is read and converted to grayscale, then a Gaussian blur is applied. This blurred, grayscale frame serves as the reference image to compare against subsequent frames.
3.  **Frame Comparison Loop:** The script enters a continuous loop where it:
      * Reads a new frame from the webcam.
      * Converts this new frame to grayscale and applies the same Gaussian blur.
      * Calculates the **absolute difference** (`cv2.absdiff`) between the current frame and the previous reference frame. This highlights areas where changes have occurred.
      * Applies a **threshold** to the difference image, converting it into a binary image where white pixels represent motion and black pixels represent no motion.
      * **Dilates** the thresholded image to expand the white areas, which helps to connect nearby motion pixels and fill in holes.
      * Finds the **contours** (outlines) of the white areas.
      * For each contour, it checks if the area is large enough (greater than 500 pixels). This filters out small, insignificant movements or noise.
      * If a contour is large enough, a green rectangle is drawn around the bounding box of that contour on the original color frame.
4.  **Display and Exit:**
      * The frame with the motion-detected rectangles is displayed in a window titled "Motion Detection".
      * The loop can be exited by pressing the 'q' key.
5.  **Cleanup:** The script releases the camera and closes all OpenCV windows upon exit.

#### Requirements

To run this script, you need to have the OpenCV library installed. You can install it using pip:

```bash
pip install opencv-python
```

#### How to Use

1.  **Install Dependencies:** Ensure you have the `opencv-python` library installed.
2.  **Run the Script:** Execute the script from your terminal:
    ```bash
    python detect_mtion.py
    ```
3.  **Camera Access:** Your webcam will turn on, and a window will appear. Any significant motion in front of the camera will be highlighted with a green rectangle.
4.  **Exit:** Press the 'q' key to stop the program and close the window.
