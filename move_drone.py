import time
from pymavlink import mavutil

print("Connecting to PX4...")
master = mavutil.mavlink_connection("udp:127.0.0.1:14540")
master.wait_heartbeat()
print("Connected")

def send_position(x, y, z):
    master.mav.set_position_target_local_ned_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111111000,
        x, y, z,
        0, 0, 0,
        0, 0, 0,
        0, 0
    )

def arm():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0
    )

def set_offboard():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_MODE,
        0,
        1, 6, 0, 0, 0, 0, 0
    )

def land():
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_NAV_LAND,
        0,
        0, 0, 0, 0, 0, 0, 0
    )

# مسار بسيط يمر بين الكرات حول القاعدة
# NED: z سالب = ارتفاع
waypoints = [
    (0.0, 0.0, -1.8),   # إقلاع فوق القاعدة
    (1.2, 0.0, -1.8),
    (1.2, 1.2, -1.8),
    (0.0, 1.6, -1.8),
    (-1.2, 1.2, -1.8),
    (-1.6, 0.0, -1.8),
    (-1.2, -1.2, -1.8),
    (0.0, -1.6, -1.8),
    (1.2, -1.2, -1.8),
    (0.0, 0.0, -1.8),   # رجوع فوق القاعدة
]

print("Sending initial setpoints...")
for _ in range(40):
    send_position(0.0, 0.0, -1.8)
    time.sleep(0.1)

print("Switching to OFFBOARD...")
set_offboard()
time.sleep(1)

print("Arming...")
arm()
time.sleep(2)

print("Starting mission...")
for wp in waypoints:
    print("Going to", wp)
    for _ in range(50):
        send_position(*wp)
        time.sleep(0.1)

print("Landing...")
land()
print("Done")


