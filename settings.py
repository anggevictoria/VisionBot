from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
ROOT = FILE.parent
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
WEBCAM = 'Webcam'
VIDEO = 'Video'

SOURCES_LIST = [IMAGE, WEBCAM, VIDEO]  

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'CENAR.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'CENAR_detected.png'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'Computer Lab 1': VIDEO_DIR / 'ComLab1.mp4',
    'Computer Setup': VIDEO_DIR / 'Computer Setup.mp4',
    'NI Elvis': VIDEO_DIR / 'NI Elvis.mp4',
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8n'

# Webcam
WEBCAM_PATH = 2
