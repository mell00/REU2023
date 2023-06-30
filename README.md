# REU2023

# DNA Image Processing 

This program performs segmentation and analyses on DNA electron microscopy images by detecting and fitting a NURBS (Non-Uniform Rational B-Spline) curve through captured DNA strands. It utilizes OpenCV, numpy, scipy, Pillow, Tkinter, and other custom modules.

## Installation

1. Clone the repository or download the program files.

2. Make sure you have Python 3.x installed on your system.

3. Install the required dependencies by running the following command: `pip install opencv-python numpy scipy`

4. Place the input image file in the same directory as the program files.

## Usage

1. Open the program file `dna_segmentation.py` in a text editor.

2. Modify the program code to specify the input image file path, color range, contour selection criteria, and other parameters as needed.

3. Save the changes.

4. Run the program by executing the following command in the terminal or command prompt: `python dna_segmentation.py`

5. The program will display the segmented DNA image with the fitted Bézier curve.

6. Close the image window to exit the program.

## Configuration

You can customize the program behavior by modifying the following parameters in the code:

- Image path: Specify the path to your input image file.
- Color range: Adjust the lower and upper bounds of the green color range to match your requirements.
- Contour selection: Set the minimum contour area and aspect ratio thresholds to filter out unwanted contours.
- Bezier curve: Modify the number of points on the fitted curve by changing the 'np.linspace' parameters.

## Dependencies

- OpenCV: Library for computer vision tasks. Install using `pip install opencv-python`.
- numpy: Library for numerical computations. Install using `pip install numpy`.
- scipy: Library for scientific computing. Install using `pip install scipy`.

## License

This program is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Madison Ell

UCLA

https://github.com/mell00

