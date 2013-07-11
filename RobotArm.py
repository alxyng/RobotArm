#	RobotArm
#
#	Written by Alex Young
#
#	A class that abstracts USB communication to the arm. When the a RobotArm object is initialised,
#	serial communication begins, possibly returning the arm to a default, known state?
#
#	Methods need to be adapted to take into consideration position and not just duration with
#	arbitrary position
#
#	Behind every great abstraction, there's a great implementation
#
#	http://www.wikihow.com/Use-a-USB-Robotic-Arm-with-a-Raspberry-Pi-(Maplin)
#
#	Before install PyUSB, libusb-1.0.0 and libusb-1.0.0-dev were installed

# import the USB and Time librarys into Python
import usb.core, usb.util, time

# Modes
PROGRAMMABLE 	= 0x00
REALTIME 		= 0x01

# Realtime status'
ON				= 0x02
OFF				= 0x03
CW 				= 0x04
ACW 			= 0x05
UP 				= 0x06
DOWN 			= 0x07
OPENING			= 0x08
CLOSING			= 0x09
STATIONARY 		= 0x0A

class RobotArm(object):
	def __init__(self):
		# Allocate the name 'serialHandle' to the USB device
		self.serialHandle = usb.core.find(idVendor = 0x1267, idProduct = 0x000)
		# Check if the arm is detected and warn if not
		if self.serialHandle is None:
			raise ValueError("Robot Arm: Device not found")
		
		# Mode
		self.mode = None
		
		# Realtime status'
		self.lightStatus = STATIONARY
		self.baseStatus = STATIONARY
		self.shoulderStatus = STATIONARY
		self.elbowStatus = STATIONARY
		self.wristStatus = STATIONARY
		self.gripStatus = STATIONARY
	
	def setMode(self, mode):
		if mode == PROGRAMMABLE:
			self.mode = PROGRAMMABLE
			return True
		elif mode == REALTIME:
			self.mode = REALTIME
			return True
		else:
			raise ValueError("Robot Arm: Incorrect mode")
	
	def controlArm(self, duration = 0):
		cmd = [0, 0, 0]
		
		if self.lightStatus == ON:
			cmd[2] = 1
		
		if self.baseStatus == CW:
			cmd[1] = 1
		elif self.baseStatus == ACW:
			cmd[1] = 2
		
		if self.shoulderStatus == UP:
			cmd[0] += 64
		elif self.shoulderStatus == DOWN:
			cmd[0] += 128
		
		if self.elbowStatus == UP:
			cmd[0] += 16
		elif self.elbowStatus == DOWN:
			cmd[0] += 32
			
		if self.wristStatus == UP:
			cmd[0] += 4
		elif self.wristStatus == DOWN:
			cmd[0] += 8
		
		if self.gripStatus == OPENING:
			cmd[0] += 2
		elif self.gripStatus == CLOSING:
			cmd[0] += 1
		
		self.serialHandle.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)
	
	def lightOn(self):
		self.lightStatus = ON
		self.controlArm()
	
	def lightOff(self):
		self.lightStatus = OFF
		self.controlArm()
		
	def lightToggle(self):
		if self.lightStatus == OFF:
			self.lightStatus = ON
		else:
			self.lightStatus = OFF
		self.controlArm()
	
	def baseStop(self):
		self.baseStatus = STATIONARY
		self.controlArm()
	
	def baseCW(self, duration = 0):
		self.baseStatus = CW
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.baseStop()
	
	def baseACW(self, duration = 0):
		self.baseStatus = ACW
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.baseStop()
	
	def shoulderStop(self):
		self.shoulderStatus = STATIONARY
		self.controlArm()
	
	def shoulderUp(self, duration = 0):
		self.shoulderStatus = UP
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.shoulderStop()
	
	def shoulderDown(self, duration = 0):
		self.shoulderStatus = DOWN
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.shoulderStop()
	
	def elbowStop(self):
		self.elbowStatus = STATIONARY
		self.controlArm()
	
	def elbowUp(self, duration = 0):
		self.elbowStatus = UP
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.elbowStop()
	
	def elbowDown(self, duration = 0):
		self.elbowStatus = DOWN
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.elbowStop()
	
	def wristStop(self):
		self.wristStatus = STATIONARY
		self.controlArm()
		
	def wristUp(self, duration = 0):
		self.wristStatus = UP
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.wristStop()
	
	def wristDown(self, duration = 0):
		self.wristStatus = DOWN
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.wristStop()
	
	def gripStop(self):
		self.gripStatus = STATIONARY
		self.controlArm()
	
	def gripOpen(self, duration = 0):
		self.gripStatus = OPENING
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.gripStop()
	
	def gripClose(self, duration = 0):
		self.gripStatus = CLOSING
		self.controlArm()
		if self.mode == PROGRAMMABLE:
			time.sleep(duration / 1000.0)
			self.gripStop()
