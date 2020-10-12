# Color-Detection
In this color detection Python project, we are going to build an application through which you can automatically get the name of the color by clicking on them.

Colors are made up of 3 primary colors; red, green, and blue. In computers, we define each color value within a range of 0 to 255.
There are approximately 16.5 million different ways to represent a color. 
We will be using a dataset that contains RGB values with their corresponding names. The CSV file for our dataset has been taken from this link: 
https://github.com/codebrainz/color-names/blob/master/output/colors.csv

OpenCV, Pandas, and numpy are the Python packages that are necessary for this project in Python. To install them, simply run this pip command in your terminal:

pip install opencv-python numpy pandas

You can run the Python file from the command prompt. Make sure to give an image path using ‘-i’ argument. If the image is in another directory, then you need to give full path of the image:

  python code.py -i add_your_image_path_here
