

import os
import shutil
import cv2
from ultralytics import YOLO


# ============================================================
# MODELLÚTVONALAK
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OBJECT_MODEL_PATH = os.path.join(BASE_DIR, "yolo26n.pt")
PLATE_MODEL_PATH = os.path.join(BASE_DIR, "models", "license_plate.pt")

# Az eredeti modell helye
FACE_MODEL_SOURCE_PATH = os.path.join(
    BASE_DIR,
    "models",
    "face_detection_yunet_2023mar.onnx"
)

# Ékezetmentes útvonal az OpenCV számára
FACE_MODEL_DIR = r"C:\SmartBlurModels"
FACE_MODEL_PATH = os.path.join(
    FACE_MODEL_DIR,
    "face_detection_yunet_2023mar.onnx"
)

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
