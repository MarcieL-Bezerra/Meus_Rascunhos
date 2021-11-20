'''import pyautogui
from PIL import ImageGrab


#x = 533 y = 491
x, y = pyautogui.position()
print("Posicao atual do mouse:")
print("x = "+str(x)+" y = "+str(y))

while True:

    tela = ImageGrab.grab() # Pega um print da tela

    # É provável que os valores range de X e Y devam ser alterados manualmente 
    for x in range(370, 400):
        #for y in range(735, 491):

        area = tela.getpixel((x, 735)) # Pega a cor do pixel (x,y)

        if area[0] == 83 or area[0] == 193:
            pyautogui.press('up') # Pula
            break

        if area[0] == 83: break'''


'''pyautogui.moveTo(100, 150)
pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
pyautogui.dragTo(100, 150)
pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down'''

import keyboard

keyboard.wait("p")
print("You pressed p")
