import pyautogui
import time
pyautogui.alert("ready to start? go to the deca answerwrite page and begin the exam before clicking yes")

for x in range(100):
    location = pyautogui.locateCenterOnScreen('image.png', confidence=0.9)