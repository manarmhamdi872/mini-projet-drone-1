import time
from pymavlink import mavutil

master = mavutil.mavlink_connection('udp:127.0.0.1:14540')

master.wait_heartbeat()
print("Connected to drone")

master.arducopter_arm()
time.sleep(2)

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0,0,0,0,0,0,5)

print("Takeoff command sent")

