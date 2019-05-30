import cv2 as cv
import numpy as np
from PIL import ImageGrab, Image
import os
import tkinter as tk
import time


if __name__ == '__main__':
    print(cv.getVersionString())
    print(np.__version__)

    recordings_dir = '/tmp/recordings/'

    if not os.path.isdir(recordings_dir):
        os.makedirs(recordings_dir)

    root = tk.Tk()
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    recording_res = (int(screen_w), int(screen_h))
    fourcc = cv.VideoWriter_fourcc(*'XVID')

    while True:
        filename = recordings_dir + time.strftime("%Y%m%d-%H%M%S") + '.avi'
        vid = cv.VideoWriter(filename, fourcc, 8, recording_res)

        while True:
            img = ImageGrab.grab(bbox=(0, 0, screen_w, screen_h))
            img.thumbnail(recording_res, Image.ANTIALIAS)
            img_np = np.array(img)
            vid.write(img_np)
            key = cv.waitKey(1)
            statinfo = os.stat(filename)
            if statinfo.st_size > 1000000000:
                break

    vid.release()
    cv.destroyAllWindows()


