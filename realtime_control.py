# Depends on the RobotArm custom class and Tkinter

# Use sudo apt-get install python-imaging python-imaging-tk

from RobotArm import *
from Tkinter import *
from ttk import *
from PIL import Image, ImageTk

arm = RobotArm()
arm.setMode(REALTIME)

root = Tk()
root.title("Robot Arm Controller")
root.geometry("800x470")
root.resizable(width = False, height = False)

app = Frame(root)

# IMAGE PART
im = Image.open('robotarm.jpg')
tkimage = ImageTk.PhotoImage(im)
Label(root, image = tkimage).pack()
# END IMAGE PART

def keyPressed(event):
	if event.keysym == 'Left':
		arm.baseCW(1000)
	elif event.keysym == 'Right':
		arm.baseACW()
	elif event.keysym == 'Up':
		arm.shoulderUp()
	elif event.keysym == 'Down':
		arm.shoulderDown()
	elif event.keysym == 'q' or event.keysym == 'Q':
		arm.elbowUp()
	elif event.keysym == 'a' or event.keysym == 'A':
		arm.elbowDown()
	elif event.keysym == 'w' or event.keysym == 'W':
		arm.wristUp()
	elif event.keysym == 's' or event.keysym == 'S':
		arm.wristDown()
	elif event.keysym == 'e' or event.keysym == 'E':
		arm.gripClose()
	elif event.keysym == 'd' or event.keysym == 'D':
		arm.gripOpen()
	elif event.keysym == 'l' or event.keysym == 'L':
		arm.lightToggle()

def keyReleased(event):
	if event.keysym == 'Left' or event.keysym == 'Right':
		arm.baseStop()
	if event.keysym == 'Up' or event.keysym == 'Down':
		arm.shoulderStop()
	if event.keysym == 'q' or event.keysym == 'a':
		arm.elbowStop()
	if event.keysym == 'w' or event.keysym == 's':
		arm.wristStop()
	if event.keysym == 'e' or event.keysym == 'd':
		arm.gripStop()
	

root.bind_all('<KeyPress>', keyPressed)
root.bind_all('<KeyRelease>', keyReleased)
root.mainloop()
