import logging
import sys
from display.display import Display

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s:%(module)s.%(filename)s,l.%(lineno)d-> %(levelname)s: %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger(__name__)
    logger.info("script has been started.")
    logger.warning("I am not an actual warning.")
    display = Display(200, 200, "StubDisplay")
    image_path = "stub_images/smiley.png"
    display.add(image_path, "smiley")
    image_path = "stub_images/sun.png"
    display.add(image_path, "sun")
    x = 0
    y = 0
    while True:
        logging.debug("I am looping now.")
        display.clear()
        display.put("smiley", x, y)
        display.put("sun", 0, 0)
        x += .01
        y += .01
        display.refresh()

