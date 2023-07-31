# WITCHES ATTACKS SPAMMER written by:
# ━━┳━━━┳━━┳━━━┳━━━━┳━━┳━━━┳━━━┳━━━╮
#┃╭━━┫╭━╮┣┫┣┫╭━╮┃╭╮╭╮┣┫┣┫╭━╮┃╭━╮┃╭━╮┃
#┃╰━━┫╰━╯┃┃┃┃┃╱╰┻╯┃┃╰╯┃┃┃┃╱┃┃╰━╯┣╯╭╯┃
#┃╭━━┫╭━━╯┃┃┃┃╱╭╮╱┃┃╱╱┃┃┃╰━╯┣━━╮┣╮╰╮┃
#┃╰━━┫┃╱╱╭┫┣┫╰━╯┃╱┃┃╱╭┫┣┫╭━╮┣━━╯┃╰━╯┃
#╰━━━┻╯╱╱╰━━┻━━━╯╱╰╯╱╰━━┻╯╱╰┻━━━┻━━━╯

import pyautogui

while True:
	pyautogui.click(x=918, y=203, clicks=1)
	print("Opening Bluestacks window")

	pyautogui.sleep(2)

	pyautogui.click(x=80, y=828, clicks=1)

	pyautogui.sleep(3)

	pyautogui.click(x=1191, y=619, clicks=1)
	print("Starting attack!")

	pyautogui.sleep(6)

	pyautogui.dragTo(x=545, y=29, duration=2)

	pyautogui.sleep(3.2)

	pyautogui.click(x=322, y=852, clicks=1)
	print("Selecting witches")

	pyautogui.sleep(1)  

	pyautogui.click(x=461, y=500, clicks=7, interval=0.2)
	print("Placing witches")

	pyautogui.click(x=187, y=831, clicks=1)
	print("Selecting war machine")

	pyautogui.sleep(int(0.75))

	pyautogui.click(x=461, y=500, clicks=1)
	print("Placing war machine")

	def activate_powerup():
		pyautogui.click(x=178, y=790, clicks=1)
		pyautogui.sleep(0.5)
		pyautogui.click(x=319, y=808, clicks=1)
		pyautogui.sleep(0.5)
		pyautogui.click(x=432, y=799, clicks=1)
		pyautogui.sleep(0.5)
		pyautogui.click(x=542, y=813, clicks=1)
		pyautogui.sleep(0.5)
		pyautogui.click(x=677, y=819, clicks=1)
		pyautogui.sleep(0.5) 
		pyautogui.click(x=771, y=819, clicks=1)
		pyautogui.sleep(0.5)  
		pyautogui.click(x=890, y=820, clicks=1)
		pyautogui.sleep(0.5)   
 
	activate_powerup()

	pyautogui.sleep(120)
	print("Attack is finished!")


	pyautogui.click(x=794, y=820, clicks=1)
	print("Returning to village!")

	pyautogui.sleep(12)
