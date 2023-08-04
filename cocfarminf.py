# ━━┳━━━┳━━┳━━━┳━━━━┳━━┳━━━┳━━━┳━━━╮
#┃╭━━┫╭━╮┣┫┣┫╭━╮┃╭╮╭╮┣┫┣┫╭━╮┃╭━╮┃╭━╮┃
#┃╰━━┫╰━╯┃┃┃┃┃╱╰┻╯┃┃╰╯┃┃┃┃╱┃┃╰━╯┣╯╭╯┃
#┃╭━━┫╭━━╯┃┃┃┃╱╭╮╱┃┃╱╱┃┃┃╰━╯┣━━╮┣╮╰╮┃
#┃╰━━┫┃╱╱╭┫┣┫╰━╯┃╱┃┃╱╭┫┣┫╭━╮┣━━╯┃╰━╯┃
#╰━━━┻╯╱╱╰━━┻━━━╯╱╰╯╱╰━━┻╯╱╰┻━━━┻━━━╯

import pyautogui

counter = 0

while True:
	counter += 1 

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
	pyautogui.sleep(4)

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


	def troops_powerup():
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
	troops_powerup()


# Activate WM Powerup 2 times with a delay of 15 seconds
	def wm_powerup():
		pyautogui.click(x=178, y=790, clicks=1)
		pyautogui.sleep(15)
		pyautogui.click(x=178, y=790, clicks=1)
	wm_powerup()


# Wait for first attack to be finished
	pyautogui.sleep(101)
	print("First attack is finished!")


# Try to place troops in 2nd attack too in case of 100%
	def troops_placement_second():
		pyautogui.click(x=1017, y=805, clicks=1)
		print("Selecting witches")
		pyautogui.sleep(1)
		pyautogui.click(x=461, y=500, clicks=7, interval=0.2)
		print("Placing witches")
		pyautogui.click(x=187, y=831, clicks=1)
		print("Selecting war machine")
		pyautogui.sleep(0.75)
		pyautogui.click(x=461, y=500, clicks=1)
		print("Placing war machine")

	def second_attack():
		print("Passing to 2nd attack")
		troops_placement_second()
		pyautogui.sleep(120)
	second_attack()


# Click on "Ritorna al villaggio!"
	pyautogui.click(x=794, y=820, clicks=1)
	print("Returning to village!")
	pyautogui.sleep(2)


# Clicking on Bonus-stella
	def claim_stars_bonus():
		pyautogui.sleep(3)
		pyautogui.click(x=783, y=735)
	claim_stars_bonus()

	
# Empty elixir attack storage
	def empty_storage():
		print("Emptying elixir storage!")
		pyautogui.moveTo(x=708, y=380)
		pyautogui.dragTo(x=724, y=781, duration=2)
		pyautogui.sleep(1)
		pyautogui.click(x=1121, y=237, clicks=1)
		pyautogui.sleep(1)
		pyautogui.click(x=1185, y=806, clicks=1)
		pyautogui.sleep(1)
		pyautogui.click(x=1364, y=87, clicks=1)
		pyautogui.sleep(1)
	empty_storage()

# Wait 2.7 seconds before starting a new attack
	pyautogui.sleep(2.7)

# Print number of attacks
	print(f" Starting attack number {counter}!")
