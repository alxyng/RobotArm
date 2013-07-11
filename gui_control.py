from RobotArm import *
from Tkinter import *

arm = RobotArm()
arm.setMode(PROGRAMMABLE)

window = Tk()
window.title("Robot Arm Nudger")
window.geometry("500x500")

t = 200;

# widget declaration
label1 = Label(window, text = "Welcome to the robot arm nudger!", relief = RAISED)
button1 = Button(window, text = "Light on", command= lambda: arm.lightOn())
button2 = Button(window, text = "Light off", command= lambda: arm.lightOff())
button3 = Button(window, text = "Nudge base cw", command= lambda: arm.baseCW(t))
button4 = Button(window, text = "Nudge base acw", command= lambda: arm.baseACW(t))
button5 = Button(window, text = "Nudge shoulder up", command= lambda: arm.shoulderUp(t))
button6 = Button(window, text = "Nudge shoulder down", command= lambda: arm.shoulderDown(t))
button7 = Button(window, text = "Nudge elbow up", command= lambda: arm.elbowUp(t))
button8 = Button(window, text = "Nudge elbow down", command= lambda: arm.elbowDown(t))
button9 = Button(window, text = "Nudge wrist up", command= lambda: arm.wristUp(t))
button10 = Button(window, text = "Nudge wrist down", command= lambda: arm.wristDown(t))
button11 = Button(window, text = "Nudge grip open", command= lambda: arm.gripOpen(t))
button12 = Button(window, text = "Nudge grip close", command= lambda: arm.gripClose(t))

# widget positioning
label1.pack(fill = BOTH, expand = 1)
button1.pack(fill = BOTH, expand = 1)
button2.pack(fill = BOTH, expand = 1)
button3.pack(fill = BOTH, expand = 1)
button4.pack(fill = BOTH, expand = 1)
button5.pack(fill = BOTH, expand = 1)
button6.pack(fill = BOTH, expand = 1)
button7.pack(fill = BOTH, expand = 1)
button8.pack(fill = BOTH, expand = 1)
button9.pack(fill = BOTH, expand = 1)
button10.pack(fill = BOTH, expand = 1)
button11.pack(fill = BOTH, expand = 1)
button12.pack(fill = BOTH, expand = 1)

# window main loop
window.mainloop()
