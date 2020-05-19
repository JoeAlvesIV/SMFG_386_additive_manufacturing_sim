# Additive Manufacturing with Robotic System 

Our goal for this project was to simulate the additive manufacturing process using an Omron TM5-700 via python programming on the RoboDK virtual replica platform as well as provide a peripheral heating bed to assist with the quality of the prints. 
The RoboDK station we developed can create a toolpath that will let you use the Omron TM5-700 as a 3D printer. The simulation allows you to create the toolpath for any object you desire as well as generate a program that can be sent to and used by the TM5-700 itself.

### Prerequisites (A step by step series of examples that tell you how to get a development env running)

Download and Acquire virtual replica software and programming platform
(What things you need to install the software and how to install them)
-VR Software: RoboDK, follow link: https://robodk.com/download 
-Programming Software: Python 64bit, follow link and select according to platform:
https://www.python.org/downloads/windows/
- Robotic Arm Model: Omron TM5-700, download via RoboDK Online Library

Create Simulation Scene
-Select File/New Station
-Add TM5-700 model into scene via Online Library
-Place 3d printed object into center of reference point
-Add Python Program into scene
-Begin customizing program to deploy additive manufacturing process


### Using RoboDK to generate toolpath
-RoboDK will generate a toolpath to 3D print objects after specifying:
	-Object to print
-Reference
-Robot
-Tool
-Approach path dimensions
-Retract path dimensions
-After specifying these you can update/generate a toolpath for printing

### Run program to simulate 3D print

The simulation uses a python program to digitally render a colored dot at places where the extruder is engaged. One must first create a robot program to call python programs for 3D printer...

Different Python programs implemented are as follows:
-Extruder.py
-FilamentSimulation.py
	-Bed_Perimiter.py
-Material_Clear.py

Extruder.py initiates the extruder. 

```
ACTION = None
import sys
if len(sys.argv) > 1:
    ACTION = float(sys.argv[1]) 
    if ACTION > 0:
        quit()

from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
RDK = Robolink()

if RDK.RunMode() != RUNMODE_SIMULATE:
    quit()

existing_material_simulation = False
info, stats_data = RDK.Spray_GetStats()
if stats_data.size(1) > 0:
    print("Spray gun statistics:")
    print(info)
    print(stats_data.tr())
    existing_material_simulation = True

```

FilamentSimulation.py Renders the desired material shapes wherever the extruder was initiated.

```
from robolink import *    
from robodk import *      


RENDER = True 
STEP_MM = 2         
STEP_DEG = 2    


RDK = Robolink()


program = RDK.ItemUserPick('Select a program to simulate', ITEM_TYPE_PROGRAM)
if not program.Valid():
    raise Exception("No program available")


robot = RDK.Item('', ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No robot available")

progname = program.Name()
print("Using program %s" % progname)

```
Bed_Perimeter.py moves the end effector in a square to show where the printer area is  and where the bed needs to be placed.

Material_Clear.py removes any material rendered from previous simulations.

After confirming correct toolpath, programs, and simulation one may send generated code to TM5-700 Robot Arm to begin additive manufacturing projects


### PID Controlled Heating bed

3D printers are able to produce better quality prints with the use of a heated bed to print on.  The heat from the bed keeps the printed parts from shrinking too rapidly which causes warping.  Warping usually causes the edges or corners of a part to curl. This can result in parts that are out of specification or can cause failures during the print itself. Our solution was to create a standalone heating bed that can operate at any temperature allowing it to be used with any 3D printing robot that doesn’t require the printing bed to move.  

To adjust the temperature press the included rotary encoder then turn to change the temperature setting. Press the encoder again to set the new temperature and the bed will adjust itself.

### PID Programming
The controller for our heating bed is arduino based which made the programming very easy. The most important part of the code are the P I and D constants.
```
//PID constants




//////////////////////////////////////////////////////////


int kp = 90;   int ki = 30;   int kd = 80;


//////////////////////////////////////////////////////////
```
These constants are extremely important and must be customized for each individual build.  The values listed here are arbitrary examples as we weren’t able to test for working values in a real life setting.

Once the code is complete it can be uploaded straight to the Arduino UNO and your heated bed is ready to go.

### PID Hardware
For this project, materials were needed to complete this. We ordered the following: 
-K-type thermocouple; Part SZZJ (qty. 5)
-Arduino UNO; Part No. 763004920050 (qty. 1)
-Thermocouple signal amplifier; Part No. MAX6675 (qty. 1)
-Rotary Encoder; Part KY - 040 (qty. 1)
-16x2 LCD; Part B019K5X530 (qty. 1)
-300x300 heating beg; Part ANET A8 PLUS E16 (qty. 1) 
-Mosfet IRF44N; Part IRFZ44NPBF (qty. 1)
-NPN BJT; Part SS8050CBU (qty. 1)
-1280 Pc. resistor pack;  Part 713665019651 (qty. 4)





## Authors

***Joe Alves**  - [JoeAlvesIV](https://github.com/JoeAlvesIV)
***Nathan Velasquez** - [nvelasquez3](https://github.com/nvelasquez3)
***Maxamiliano Garcia** [] (mgarcia161@mail.csuchico.edu) 
