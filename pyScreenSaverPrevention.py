#!python3
import pyautogui
import sys

# constants
MOVE_DISTSANCE = 60

# method
pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

def main():
    """main process
    """
    # 画面中央に移動
    screen_pos = pyautogui.size()
    center_x = screen_pos.width / 2
    center_y = screen_pos.height / 2
    pyautogui.moveTo(center_x,center_y)

    try:
        x,y = pyautogui.position()

        while True:
            pyautogui.moveTo(x, y + MOVE_DISTSANCE, duration=0.2)
            pyautogui.moveTo(x - MOVE_DISTSANCE, y + MOVE_DISTSANCE, duration=0.2)
            pyautogui.moveTo(x - MOVE_DISTSANCE, y, duration=0.2)
            pyautogui.moveTo(x, y, duration=0.2)
            pyautogui.press('ctrl')

    except KeyboardInterrupt:
        print('end')


if __name__ == "__main__":
    main()
