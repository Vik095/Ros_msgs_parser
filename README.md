# Ros_msgs_parser

Messages/ directoring includes all .msg files from the following packages:
- actionlib_msgs
- diagnostic_msgs
- geometry_msgs
- mavros_msgs
- mess_msgs
- nav_msgs
- sensor_msgs
- shape_msgs
- std_msgs
- stereo_msgs
- trajectory_msgs
- turtlebot3_msgs
- visualization_msgs

# Purpose
Universal ROS data logger that works with standard ROS messages

# How to use
Import breaker then do breaker.process(msgtype, "<name of message>"). This returns the entire structure of the specified message type to ROS-primitive data types. 
