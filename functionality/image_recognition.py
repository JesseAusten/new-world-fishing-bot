from numpy import array
import cv2 as cv
from PIL import ImageGrab
from utils.global_variables import WAITING_FOR_FISH, FISH_NOTICED
from wrappers.logging_wrapper import debug

NOTHING = cv.imread(WAITING_FOR_FISH)
NOTICE = cv.imread(FISH_NOTICED)
REEL_COLOR = (14, 181, 133)
WAIT_COLOR_BROWN = (173, 92, 32)
WAIT_COLOR_RED = (62, 16, 18)
COLOR_WAGES = 7

def image_recognition_result(x, y, width, height):
    region=(x, y, x + width, y + height)
    img = ImageGrab.grab(bbox = region)
    img_cv = cv.cvtColor(array(img), cv.COLOR_RGB2BGR)
    res = cv.matchTemplate(img_cv, NOTHING, eval('cv.TM_CCOEFF_NORMED'))
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    debug(f'max_val waiting is {max_val}')
    if max_val >= 0.7:
        return '0'
    res = cv.matchTemplate(img_cv, NOTICE, eval('cv.TM_CCOEFF_NORMED'))
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    debug(f'max_val caught is {max_val}')
    if max_val >= 0.7:
        return '1'

    g = 0
    b = 0
    r = 0
    for i in range(width):
        for j in range(height):
            color = img.getpixel((i, j))
            if pixel_match(color, REEL_COLOR):
                g += 1
            if pixel_match(color, WAIT_COLOR_BROWN):
                b += 1
            if pixel_match(color, WAIT_COLOR_RED):
                r += 1

    debug(f'g,b,r: ({g}, {b}, {r})')

    if g == max(g, b, r) and g > 3:
        debug('green')
        return '2'
    if b == max(g, b, r) and b > 3:
        debug('brown')
        return '3'
    if r == max(g, b, r) and r > 3:
        debug('red')
        return '3'

    debug('nothing')
    return '4'

def pixel_match(color, matcher):
    for i in range (0,3):
        if not((matcher[i] - COLOR_WAGES) <= color[i] <= (matcher[i] + COLOR_WAGES)):
            return False
    return True
