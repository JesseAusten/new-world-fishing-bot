from utils.config import dict, random_timeout
from time import sleep
from wrappers.win32api_wrapper import *
from wrappers.logging_wrapper import debug
import random

is_b_pressed = False

def fish_notice():
    notice_timeout = random_timeout(dict['fishing']['timeouts']['notice'])
    debug("Press mouse key for: {} s".format(notice_timeout))
    press_mouse_key()
    sleep(notice_timeout)
    release_mouse_key()

def reel_fish():
    global is_b_pressed
    if not is_b_pressed:
        sleep(max(0.05, random.gauss(0.2, 0.1)))
        debug("press b")
        press_key('b')
        is_b_pressed = True
    reel_timeout = random_timeout(dict['fishing']['timeouts']['reeling'])
    debug("Press mouse key for: {} s".format(reel_timeout))
    press_mouse_key()
    sleep(reel_timeout)
    release_mouse_key()

def pause():
    pause_timeout = random_timeout(dict['fishing']['timeouts']['pause'])
    debug("Pause for: {} s".format(pause_timeout))
    sleep(pause_timeout)

def cast():
    cast_timeout = random_timeout(dict['fishing']['timeouts']['cast'])
    debug("Pause for: 8 s")
    sleep(max(0.05, 8 + random.gauss(0.1, 0.05)))
    global is_b_pressed
    if is_b_pressed:
        debug("release b")
        release_key('b')
        is_b_pressed = False
        sleep(max(0.05, random.gauss(0.3, 0.07)))
    press_mouse_key()
    sleep(cast_timeout)
    release_mouse_key()
    debug("Pause for: 4 s")
    sleep(max(0.05, 4 + random.gauss(0.1, 0.05)))

def repairing():
    release_key('b')
    arm_disarm_timeout = random_timeout(dict['repairing']['timeouts']['arm_disarm'])
    debug("Disarm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(arm_disarm_timeout)

    inventory_timeout = random_timeout(dict['repairing']['timeouts']['inventory'])
    debug("Open inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(inventory_timeout)

    repair_timeout = random_timeout(dict['repairing']['timeouts']['repair'])
    debug("Repair fishing rod. Total time: {} s".format(repair_timeout))
    repair(repair_timeout)

    confirm_timeout = random_timeout(dict['repairing']['timeouts']['confirm'])
    debug("Confirm repair. Total time: {} s".format(confirm_timeout))
    confirm_repair(confirm_timeout)

    debug("Close inventory. Total time: {} s".format(inventory_timeout))
    open_close_inventory(inventory_timeout)

    debug("Arm fishing rod. Total time: {} s".format(arm_disarm_timeout))
    arm_disarm_fishing_rod(arm_disarm_timeout)

def arm_disarm_fishing_rod(timeout):
    sleep(timeout)
    press_key('F3')
    sleep(max(0.05, random.gauss(0.09, 0.02)))
    release_key('F3')
    sleep(timeout)

def open_close_inventory(timeout):
    sleep(timeout)
    press_key('tab')
    sleep(max(0.05, random.gauss(0.09, 0.02)))
    release_key('tab')
    sleep(timeout)

def repair(timeout):
    sleep(timeout)
    press_key('r')
    sleep(max(0.05, random.gauss(0.2, 0.1)))
    click_mouse_with_coordinates(dict['repairing']['x'].get(), dict['repairing']['y'].get())
    sleep(max(0.05, random.gauss(0.1, 0.05)))
    release_key('r')
    sleep(timeout)

def confirm_repair(timeout):
    sleep(timeout)
    press_key('e')
    sleep(max(0.05, random.gauss(0.09, 0.02)))
    release_key('e')
    sleep(timeout)
