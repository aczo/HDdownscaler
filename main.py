# Downscales files in 4K and 1080p to 720p
import os, argparse, pathlib

os.environ["OPENCV_LOG_LEVEL"]="SILENT"
import cv2

parser = argparse.ArgumentParser(description = "Lists video files with at least FHD (1080p) resolution for downscaling")
parser.add_argument('path', type=pathlib.Path, help='Directory containing files to be downscaled')
args = parser.parse_args()

path = args.path
files = [f for f in os.listdir(path) if os.path.isfile(path / f)]

total_size = 0
i = 0
e = 0
for f in files:
    osfullpath = str(path / f)
    try:
        vid = cv2.VideoCapture()
        vid.setExceptionMode(True)
        vid.open(osfullpath)
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        #  print(" {}x{}".format(width, height), end="")
        vid.release()
        if height >= 1080 and width >= 1920:
            i += 1
            size = os.path.getsize(path / f)
            print("{}|{}|{}".format(i, str(f), size))
            total_size += size
    except Exception as exc:
        e += 1
print("Total size of all files eligible for conversion is {} GB.".format(total_size/1024/1024/1024))