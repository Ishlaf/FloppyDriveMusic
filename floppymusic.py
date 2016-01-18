###############################################################################
##                          Floppy Drive 34 Pin Setup                        ##
##             2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34             ##
##             1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33             ##
##                                                                           ##
##                    Pin |  Name  | Direction |    Description              ##
##                     2  | /REDWC |    --->   |  Density Select             ##
##                     4  |   n/c  |           |     Reserved                ##
##                     6  |   n/c  |           |     Reserved                ##
##                     8  | /INDEX |   <---    |       Index                 ##
##                    10  | /MOTEA |    --->   |   Motor Enable A            ##
##                    12  | /DRVSB |    --->   |    Drive Sel B              ##
##                    14  | /DRVSA |    --->   |    Drive Sel A              ##
##                    16  | /MOTEB |    --->   |   Motor Enable B            ##
##                    18  |  /DIR  |    --->   |     Direction               ##
##                    20  |  /STEP |    --->   |       Step                  ##
##                    22  | /WDATE |    --->   |     Write Data              ##
##                    24  | /WGATE |    --->   | Floppy Write Enable         ##
##                    26  | /TRK00 |   <---    |      Track 0                ##
##                    28  |  /WPT  |   <---    |    Write Protect            ##
##                    30  | /RDATA |   <---    |      Read Data              ##
##                    32  | /SIDE1 |    --->   |     Head Select             ##
##                    34  | /DSKCHG|   <---    |  Disk Change/Ready          ##
##                   Odds |   GND  |           |       Ground                ##
##                                                                           ##
##                         Important Pins: 12, 18, 20                        ##
###############################################################################

import RPi.GPIO as GPIO
import time

# Initializes GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Class for managing floppy drive data and movement
class floppydrive:
    def __init__(self, maxsteps, s, d, l):
        self.maxsteps = maxsteps  # Stores max num of steps in a direction
        self.s = s                # Stores pin for steps
        self.d = d                # Stores pin for direction
        self.l = l                # Stores pin for light/power state
        self.pos = 1              # Stores position of arm
        self.direction = 1        # Stores direction arm will move

        # Initializes pins used for step/direction/light
        GPIO.setup(s, GPIO.OUT)
        GPIO.setup(d, GPIO.OUT)
        GPIO.setup(l, GPIO.OUT)

        # Turns drive off
        self.off()

    # Changes direction of arm
    def change_direction(self):
        self.direction = -self.direction

        # Changes power state of direction pin from on to off and vise versa
        GPIO.output(self.d, 1-GPIO.input(self.d))

    # Moves arm one step
    def step(self):
        # Checks arm location and changes direction if needed
        if (self.pos == 1 and self.direction == -1) or (self.pos == self.maxsteps and self.direction == 1):
            self.change_direction()

        # Pulses step pin once
        GPIO.output(self.s, 0)
        GPIO.output(self.s, 1)
        GPIO.output(self.s, 0)

        # Stores new arm position
        self.pos += self.direction

    # Moves arm as far back as possible and changes variables accordingly
    def reset(self):
        self.on()

        # Changes direction to go backwards
        GPIO.output(self.d, 1)

        # Pulses step for 5 times the max number of steps
        for i in range(self.maxsteps*5):
            GPIO.output(self.s, 0)
            GPIO.output(self.s, 1)
            time.sleep(.01)

        # Changes direction to go forwards
        GPIO.output(self.d, 0)

        # Resets position and direction variables
        self.pos = 1
        self.direction = 1

        self.off()

    # Turns drive on
    def on(self):
        # Turns power/light pin on
        GPIO.output(self.l,0)

    def off(self):
        # Turns power/light pin off
        GPIO.output(self.l,1)

# Pulses drive (d) at a frequency (htz) for t seconds
def note(htz, t, d):
     # Calculates length between pulses
     l = 1.0/htz

      # Calculates number of pulses
     times = htz*t

     d.on()

     # Pulses drive calculated number of times at correct frequency
     for i in range(int(times)):
             d.step()
             time.sleep(l)

     # Min time between notes (up for change)
     time.sleep(.05)

     d.off()

# Mary had a little lamb (WIP)
def mary(drive):
    note(330, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(262, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(330, 2, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(294, 2, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(330, 2, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(262, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(262, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(330, 1, drive)
    time.sleep(0.05)
    note(294, 1, drive)
    time.sleep(0.05)
    note(262, 2, drive)
    time.sleep(0.05)

# Imperial March (WIP)
def imperial(drive):
    note(98,.5,drive)
    note(98,.5,drive)
    note(98,.5,drive)
    note(82.41,.375,drive)
    note(116.54,.125,drive)
    note(98,.5,drive)
    note(82.41,.375,drive)
    note(116.54,.125,drive)
    note(98,1,drive)
    note(146.83,.5,drive)
    note(146.83,.5,drive)
    note(146.83,.5,drive)
    note(155.56,.375,drive)
    note(116.54,.125,drive)
    note(92.5,.5,drive)
    note(82.41,.375,drive)
    note(116.54,.125,drive)
    note(98,1,drive)
    note(196,.5,drive)
    note(98,.375,drive)
    note(98,.125,drive)
    note(196,.5,drive)
    note(185,.375,drive)
    note(174.61,.125,drive)
    note(164.81,.125,drive)
    note(155.56,.125,drive)
    note(164.81,.25,drive)
    time.sleep(.25)
    note(103.83,.25,drive)
    note(138.59,.5,drive)
    note(130.81,.375,drive)
    note(123.47,.125,drive)
    note(116.54,.125,drive)
    note(110,.125,drive)
    note(116.54,.25,drive)
    time.sleep(.25)
    note(77.78,.25,drive)
    note(92.5,.5,drive)
    note(77.78,.375,drive)
    note(92.5,.125,drive)
    note(116.54,.5,drive)
    note(92.5,.375,drive)
    note(116.54,.125,drive)
    note(146.83,1,drive)

# Cantina Song (WIP)
def cantina(drive):
    note(220, .5, drive)
    note(293.66, .5, drive)
    note(220, .5, drive)
    note(293.66, .5, drive)
    note(220, .25, drive)
    note(293.66, .5, drive)
    note(220, .25, drive)
    time.sleep(.25)
    note(207.65, .25, drive)
    note(220, .5, drive)
    note(220, .25, drive)
    note(207.65, .25, drive)
    note(220, .25, drive)
    note(196, .25, drive)
    time.sleep(.25)
    note(185, .25, drive)
    note(196, .25, drive)
    note(185, .25, drive)
    note(174.61, .75, drive)
    note(146.83, .25, drive)
    note(146.83, 1, drive)
    note(220, .5, drive)
    note(293.66, .5, drive)
    note(220, .5, drive)
    note(293.66, .5, drive)
    note(220, .25, drive)
    note(293.66, .5, drive)
    note(220, .25, drive)
    time.sleep(.25)
    note(207.65, .25, drive)
    note(220, .5, drive)
    note(196, .25, drive)
    time.sleep(.25)
    note(196, .75, drive)
    note(185, .25, drive)
    note(196, .5, drive)
    note(261.63, .25, drive)
    note(233.08, .5, drive)
    note(220, .5, drive)
    note(196, .75, drive)
    note(220, .5, drive)
    note(293.66, .5, drive)
    note(220, .5, drive)
    note(293.66, .5, drive)
    note(220, .25, drive)
    note(293.66, .5, drive)
    note(220, .25, drive)
    time.sleep(.25)
    note(207.65, .25, drive)
    note(220, .5, drive)
    note(261.63, .25, drive)
    time.sleep(.25)
    note(261.63, .75, drive)
    note(220, .25, drive)
    note(196, .5, drive)
    note(174.61, .5, drive)
    note(146.83, 1.25, drive)
    note(146.83, 1, drive)
    note(174.61, 1, drive)
    note(220, 1, drive)
    note(261.63, 1, drive)
    note(311.13, .5, drive)
    note(293.66, .5, drive)
    note(207.65, .25, drive)
    note(220, .5, drive)
    note(174.61, 2.25, drive)
    time.sleep(.25)
    note(440, .5, drive)
    note(349.23, .25, drive)
    note(440, .5, drive)
    time.sleep(.75)
    note(440, .5, drive)
    note(349.23, .25, drive)
    note(440, .5, drive)
    time.sleep(.75)
    note(440, .5, drive)
    note(349.23, .25, drive)
    note(415.3, .25, drive)
    note(440, .5, drive)
    note(349.23, 1.25, drive)
    note(293.66, 1, drive)
    time.sleep(.25)
    note(440, .5, drive)
    note(349.23, .25, drive)
    note(440, .5, drive)
    time.sleep(.75)
    note(440, .5, drive)
    note(349.23, .25, drive)
    note(440, .5, drive)
    time.sleep(.75)
    note(440, .5, drive)
    note(349.23, .25, drive)
    note(415.3, .25, drive)
    note(392, .5, drive)
    note(392, 1.25, drive)
    note(261.63, 1, drive)
