# This script will simulate the final result of the 3D printed part using the Spray function

# Or visit: http://www.robodk.com/doc/PythonAPI/
# Note: you do not need to keep a copy of this file, your python script is saved with the station
from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations


RENDER = True      # Set to False 
STEP_MM = 2         # Detail step in MM for linear moves
STEP_DEG = 2        # Detail step in DEG for joint moves

# Start a connection with the RoboDK API
RDK = Robolink()

# Select the first/only robot in the cell:
program = RDK.ItemUserPick('Select a program to simulate', ITEM_TYPE_PROGRAM)
if not program.Valid():
    raise Exception("No program available")

# Get the robot
robot = RDK.Item('', ITEM_TYPE_ROBOT)
#robot = program.getLink(ITEM_TYPE_ROBOT) # available in newer versions
if not robot.Valid():
    raise Exception("No robot available")

progname = program.Name()
print("Using program %s" % progname)


# Get the program as a list of joint values
tool = robot.getLink(ITEM_TYPE_TOOL)
progok_jlist = program.InstructionListJoints(STEP_MM, STEP_DEG)
progok = progok_jlist[0] # progok: String that indicates if there are any issues with the program
jlist = progok_jlist[1]  # jlist: list of joints

# Check that the program is correct and has at least a movement
njoints = jlist.size(1)
if njoints < 1:
    raise Exception("Program %s has no movements" % name)

# Check if there are any issues with the program:
if progok != "Success":
    raise Exception("Problems with program %s: %s." %(name, progok))

# Reset any material deposition simulation
RDK.Spray_Clear()

robot.setPoseTool(tool)

# Start material deposition simulation according to the Extruder script
RDK.RunProgram('Extruder(0)')
# Alternatively:
#RDK.Item('Extruder', ITEM_TYPE_PYTHON).RunProgram([1])

if not RENDER:
    RDK.Render(False)

# Iterate through all joints in the matrix and check for collisions
njoints_all = jlist.size(1)       
for i in range(njoints_all):
    ji = jlist[:,i].tolist()
    
    # Update the robot to a new position (it will create a new particle)
    robot.setJoints(ji)
    if not RENDER:
        # If Render is turned off (faster) update the position to draw a new particle
        RDK.Update()
    
    # Show a message in the RoboDK status bar from time to time
    if i % 10 == 0:
        msg = "Quick material deposition simulation for %s (%.1f %%)" % (progname, 100.0*(i/njoints_all))
        print(msg)
        RDK.ShowMessage(msg, False)

    # Render from time to time even if we have render deactivated
    if not RENDER and i % 500 == 0:
        RDK.Render()

RDK.Render(True)       
msg = "Done"
print("Done")
RDK.ShowMessage(msg, False)
