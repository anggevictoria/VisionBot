# <span style="color:deepskyblue"> VISIONBOT </span>

This website titled VISIONBOT is a web application that merges real-time object detection with conversational AI, creating a dynamic and interactive user experience. This project draws inspiration from two open-source projects:

Object Detection and Tracking with YOLOv8 and Streamlit - A seamless integration of YOLOv8, a leading object detection algorithm, with Streamlit, a Python web application framework for building intuitive and interactive web apps. Explore the original project here: https://github.com/rampal-punia/yolov8-streamlit-detection-tracking.git 

Streaming Local LLM Responses with LM Studio - A powerful implementation of local Large Language Model (LLM) responses via the LM Studio Inference Server, enabling responsive, privacy-focused AI interactions. Explore the original project here: https://github.com/ingridstevens/AI-projects.git 


## <span style="color:deepskyblue">DEMO</span>
https://drive.google.com/file/d/1ZmW1NGMcfEYOIWeJ5Yx4Q3m8TBiYMknD/view?usp=sharing 

## <span style="color:deepskyblue">WebApp Demo on Streamlit Server</span>

This app is up and running on Streamlit cloud server!!! You can check the demo of this web application on this link 
[yolov8-streamlit-detection-tracking-webapp](https://yolov8-object-detection-and-tracking-app.streamlit.app/)

**Note**: In the demo, Due to large size of custom model, cocodataset was used but you can find the custom model used in the demo here: 


## Requirements

Python 3.6+
YOLOv8
Streamlit

```bash
pip install ultralytics streamlit pytube
```

## Installation

- Clone the repository: git clone <https://github.com/CodingMantras/yolov8-streamlit-detection-tracking.git>
- Change to the repository directory: `cd yolov8-streamlit-detection-tracking`
- Create `weights`, `videos`, and `images` directories inside the project.
- Download the pre-trained YOLOv8 weights from (<https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>) and save them to the `weights` directory in the same project.

## Usage

- Run the app with the following command: `streamlit run app.py`
- The app should open in a new browser window.

### Detection on images

- The default image with its objects-detected image is displayed on the main page.
- Select a source. (radio button selection `Image`).
- Upload an image by clicking on the "Browse files" button.
- Click the "Detect Objects" button to run the object detection algorithm on the uploaded image with the selected confidence threshold.
- The resulting image with objects detected will be displayed on the page. Click the "Download Image" button to download the image.("If save image to download" is selected)

## Detection in Videos

- Create a folder with name `videos` in the same directory
- Dump your videos in this folder
- In `settings.py` edit the following lines.

```python
# video
VIDEO_DIR = ROOT / 'videos' # After creating the videos folder

# Suppose you have four videos inside videos folder
# Edit the name of video_1, 2, 3, 4 (with the names of your video files) 
VIDEO_1_PATH = VIDEO_DIR / 'video_1.mp4' 
VIDEO_2_PATH = VIDEO_DIR / 'video_2.mp4'
VIDEO_3_PATH = VIDEO_DIR / 'video_3.mp4'
VIDEO_4_PATH = VIDEO_DIR / 'video_4.mp4'

# Edit the same names here also.
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH,
    'video_2': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
    'video_4': VIDEO_4_PATH,
}

# Your videos will start appearing inside streamlit webapp 'Choose a video'.
```

- Click on `Detect Video Objects` button and the selected task (detection/segmentation) will start on the selected video.

### Detection on RTSP

- Select the RTSP stream button
- Enter the rtsp url inside the textbox and hit `Detect Objects` button

## Acknowledgements

This app uses [YOLOv8](<https://github.com/ultralytics/ultralytics>) for object detection algorithm and [Streamlit](<https://github.com/streamlit/streamlit>) library for the user interface.

### Disclaimer

This project is intended as a learning exercise and demonstration of integrating various technologies, including:

- Streamlit
- YoloV8
- Object-Detection on Images And Live Video Streams
- Python-OpenCV

Please note that this application is not designed or tested for production use. It serves as an educational resource and a showcase of technology integration rather than a production-ready web application.

Contributors and users are welcome to explore, learn from, and build upon this project for educational purposes.

### Hit star ⭐ if you like this repo!!!
