# WITCHES ATTACKS SPAMMER written by:
# ━━┳━━━┳━━┳━━━┳━━━━┳━━┳━━━┳━━━┳━━━╮
#┃╭━━┫╭━╮┣┫┣┫╭━╮┃╭╮╭╮┣┫┣┫╭━╮┃╭━╮┃╭━╮┃
#┃╰━━┫╰━╯┃┃┃┃┃╱╰┻╯┃┃╰╯┃┃┃┃╱┃┃╰━╯┣╯╭╯┃
#┃╭━━┫╭━━╯┃┃┃┃╱╭╮╱┃┃╱╱┃┃┃╰━╯┣━━╮┣╮╰╮┃
#┃╰━━┫┃╱╱╭┫┣┫╰━╯┃╱┃┃╱╭┫┣┫╭━╮┣━━╯┃╰━╯┃
#╰━━━┻╯╱╱╰━━┻━━━╯╱╰╯╱╰━━┻╯╱╰┻━━━┻━━━╯

import pyautogui

while True:
# Selecting Bluestacks window
	pyautogui.click(x=918, y=203, clicks=1)
	print("Opening Bluestacks window")
	pyautogui.sleep(2)


# Click on "Attacco!"
	pyautogui.click(x=80, y=828, clicks=1)
	pyautogui.sleep(2.5)

# Click on "Cerca!"
	pyautogui.click(x=1191, y=619, clicks=1)
	print("Starting attack!")
	pyautogui.sleep(5)

# Drag to ultimate bottom-right to find good troop-placing angle
	pyautogui.dragTo(x=545, y=29, duration=2)
	pyautogui.sleep(2.7)



	def troops_placement():
		pyautogui.click(x=322, y=852, clicks=1)
		print("Selecting witches")
		pyautogui.sleep(1)

		pyautogui.click(x=461, y=500, clicks=7, interval=0.2)
		print("Placing witches")

		pyautogui.click(x=187, y=831, clicks=1)
		print("Selecting war machine")

		pyautogui.sleep(0.75)

		pyautogui.click(x=461, y=500, clicks=1)
		print("Placing war machine")

	troops_placement()



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


# Click on "Ritorna al villaggio!"
	pyautogui.click(x=794, y=820, clicks=1)
	print("Returning to village!")

# Wait 7.3 seconds before starting a new attack
	pyautogui.sleep(7.3)