Project Name:
Obstacle Avoidance with LiDAR - Drone Robot

Project Introduction:
This project is a drone simulation developed using ROS 2, PX4, and Gazebo.
The drone is programmed to fly automatically through predefined points and rings inside a custom simulation world.
The objective of the project is to demonstrate autonomous drone navigation and movement control in a simulated environment.

Description:
This project is a ROS 2 / PX4 / Gazebo simulation of an X500 drone.
The drone is launched in Gazebo using PX4 SITL, then controlled using a Python script.

Terminal 1: Launch PX4 SITL with Gazebo

cd PX4-Autopilot
make px4_sitl gz_x500

Wait until Gazebo opens and the message appears:

Ready for take off

Terminal 2: Run the drone movement script

cd PX4-Autopilot
python3 move_drone.py


If the drone does not move:

In Terminal 1, force the system to arm and take off:

param set COM_ARM_WO_GPS 1
param set COM_ARM_MAG 0
param set COM_ARM_IMU_ACC 0
param set COM_ARM_IMU_GYR 0
commander arm -f
commander takeoff

Then in Terminal 2, run again:

python3 move_drone.py


Technical problem solution:

Sometimes the problem is caused by old Gazebo or PX4 processes still running in the background.

First, stop all terminals using:

CTRL + C

Then open a new terminal and run:

pkill -f px4
pkill -f gz
pkill -f gazebo
ps aux | grep gz

After that, launch the simulation again:

cd PX4-Autopilot
PX4_GZ_WORLD=drone_world make px4_sitl gz_x500

Then open Terminal 2 and run:

cd PX4-Autopilot
python3 move_drone.py


Useful PX4 commands:

commander land
Used to land the drone.

commander arm -f
Used to arm the motors.

commander takeoff
Used to take off.

commander disarm
Used to stop the motors after landing.


Notes:
- Terminal 1 must stay open while the simulation is running.
- Terminal 2 is used to run the movement script.
- If Gazebo does not open correctly or the drone does not respond, close all old processes and restart the simulation.
- Always wait for the message "Ready for take off" before running the Python script.

