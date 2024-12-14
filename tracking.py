import socketio
import cv2
import numpy as np
import base64
import time
from pymavlink import mavutil
from threading import Thread, Event
from picamera2 import Picamera2


def request_message_interval():

def get_alt():
def takeoff(alt: float):
def trigger_yaw_thread(angle_distance: int = 0):
def trigger_distance_thread():


while main_event.is_set():
    frame=picam2.capture_array()
    
    _, frame_data = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
    base64_frame = base64.b64encode(frame_data).decode("utf-8")
    sio.emit("video", base64_frame)

    time.sleep(0.2)

vehicle.mav.command_long_send(
    vehicle.target_system,
    vehicle.target_component,
    mavutil.mavlink.MAV_CMD_NAV_LAND,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
)
