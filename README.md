# Gender Detection with DeepFace and OpenCV

This project detects the gender (male or female) in images using the **DeepFace** library for facial recognition and **OpenCV** for face detection. The system scans a folder of images, detects faces, and classifies the gender of each person in the images.

## Requirements

Before running the project, install the necessary dependencies:

pip install opencv-python
pip install deepface
pip install tensorflow
If you prefer to use PyTorch as the backend for DeepFace, install it as well:


pip install torch torchvision
How to Use
Clone the repository or download the files to your local machine.

Place the images you want to process inside a folder.

Modify the folder_path variable in the main.py file to point to the directory containing your images:



folder_path = 'path/to/your/folder'
Run the main.py script:


python src/main.py
The script will iterate over all images in the specified folder, detect faces, and display the detected gender (male or female) for each face found. The processed images will be saved with the prefix output_ in the same directory.

Example Output
After execution, you will see an output similar to this:

Image: path/to/image.jpg -> Detected gender: Female
Image: path/to/another_image.jpg -> Detected gender: Male
Processed images will be saved in the same folder with the prefix output_.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Special thanks to:

OpenCV: Open Source Computer Vision Library.
DeepFace: A Python library for deep learning facial recognition.
TensorFlow: Backend for facial recognition.
