

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


# ============================================================
# YUNET MODELL MÁSOLÁSA ÉKEZETMENTES ÚTVONALRA
# ============================================================

def prepare_face_model():
    if not os.path.exists(FACE_MODEL_SOURCE_PATH):
        raise FileNotFoundError(
            f"Nem található az arcfelismerő modell: {FACE_MODEL_SOURCE_PATH}"
        )

    os.makedirs(FACE_MODEL_DIR, exist_ok=True)

    source_size = os.path.getsize(FACE_MODEL_SOURCE_PATH)

    target_needs_copy = (
        not os.path.exists(FACE_MODEL_PATH)
        or os.path.getsize(FACE_MODEL_PATH) != source_size
    )

    if target_needs_copy:
        shutil.copyfile(
            FACE_MODEL_SOURCE_PATH,
            FACE_MODEL_PATH
        )

    if not os.path.exists(FACE_MODEL_PATH):
        raise FileNotFoundError(
            f"A YuNet modell nem található: {FACE_MODEL_PATH}"
        )

    print(f"YuNet modell előkészítve: {FACE_MODEL_PATH}")


# ============================================================
# MODELLEK BETÖLTÉSE
# ============================================================

print("SmartBlur modellek betöltése...")

object_model = YOLO(OBJECT_MODEL_PATH)
plate_model = YOLO(PLATE_MODEL_PATH)

prepare_face_model()

print("SmartBlur modellek sikeresen betöltve!")

