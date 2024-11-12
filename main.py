import pyautogui
import time
pyautogui.alert("ready to start? go to the deca answerwrite page and begin the exam before clicking yes")

for x in range(100):
    location = pyautogui.locateCenterOnScreen('image.png', confidence=0.9)
    pyautogui.click(location)

    try:
        click = pyautogui.locateCenterOnScreen('b.png', confidence=0.6)
        pyautogui.click(click)
    except:
        try:
            click = pyautogui.locateCenterOnScreen('c.png', confidence=0.6)
            pyautogui.click(click)
        except:
            try:
                click = pyautogui.locateCenterOnScreen('d.png', confidence=0.6)
                pyautogui.click(click)
            except:
                continue
    time.sleep(0.1)
    next = pyautogui.locateCenterOnScreen('next.png', confidence=0.9)
    pyautogui.click(next)