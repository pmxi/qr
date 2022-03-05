import cv2
import numpy as np
from pyzbar.pyzbar import decode


def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        v.add(barcodeData)

        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)

        cv2.putText(
            frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2
        )
        # print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        # print(barcodeData)


def save():
    scoutingFile = open("scouting.txt", "a")

    if len(v) != 0:
        for i in v:
            scoutingFile.write(i + "\n")
        print("SAVED! ( ͡° ͜ʖ ͡°)\n")
    else:
        print("SAVED NOTHING! ¯\\_(ツ)_/¯\n")

    scoutingFile.close()


cap = cv2.VideoCapture(0)

v = set()
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow("Image", frame)
    code = cv2.waitKey(10)
    if code == ord("q"):
        print("Saving! (O.o)\n         /||\\\n         / \\")
        save()
        v.clear()
