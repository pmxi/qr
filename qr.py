import cv2
# import numpy as np
from numpy import array, int32
from pyzbar.pyzbar import decode
import argparse

parser = argparse.ArgumentParser(description="qr code scanner to text file")
parser.add_argument("-f", "--file", type=str,default="scouting.txt", help="file to output qr code scans to, relative or absolute")
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()


def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        # pts = np.array(points, np.int32)
        pts = array(points, int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        v.add(barcodeData)

        barcodeType = obj.type
        string = str(barcodeData) + " | Type " + str(barcodeType)

        cv2.putText(
            frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2
        )
        if args.verbose:
            print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        # print(barcodeData)


def save(values: set):
    with open(args.file, "a") as scouting_file:
        if len(v) != 0:
            for i in v:
                scouting_file.write(i + "\n")
            print("SAVED! ( ͡° ͜ʖ ͡°)\n")
        else:
            print("SAVED NOTHING! ¯\\_(ツ)_/¯\n")


cap = cv2.VideoCapture(0)

v = set()

while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow("QR SCANNER", frame)
    code = cv2.waitKey(10)
    if code == ord("q"):
        print("Saving! (O.o)\n         /||\\\n         / \\")
        save(v)
        v.clear()
    elif code == ord("s"):
        for i in v:
            print(i)
    elif code == ord("c"):
        break
