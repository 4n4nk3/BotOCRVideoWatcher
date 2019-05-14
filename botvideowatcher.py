from my_clicker import *
from my_ocr import *
import mss
import mss.tools
from time import sleep

while 1:
    sleep(5)
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 1011, "left": 2651, "width": 34, "height": 14}
        output = "immagine.png"

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)
        timer = ocr_scan(output)
        print(timer)
        sleep(timer)
        next()
