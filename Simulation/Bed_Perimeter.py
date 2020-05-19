# Type help("robolink") or help("robodk") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/index.html
# Note: It is not required to keep a copy of this file, your python script is saved with the station
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
RDK = Robolink()

robot = RDK.Item('', ITEM_TYPE_ROBOT)

home = RDK.Item('Home')
target_1 = RDK.Item('Target 1')
target_2 = RDK.Item('Target 4')
target_3 = RDK.Item('Target 2')
target_4 = RDK.Item('Target 3')
robot.MoveL(home)

robot.MoveL(target_1)
pause(20)
robot.MoveL(target_2)
pause(20)
robot.MoveL(target_3)
pause(20)
robot.MoveL(target_4)
pause(20)
robot.MoveL(target_1)
pause(20)
robot.MoveL(target_2)
pause(20)
robot.MoveL(target_3)
pause(20)
robot.MoveL(target_4)
pause(20)
robot.MoveL(home)
