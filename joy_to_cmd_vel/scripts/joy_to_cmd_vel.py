#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Initialize velocity values
linear_velocity = 0.0
angular_velocity = 0.0

# Create a Twist message
msg = Twist()

# Define the callback function for joystick input
def joy_callback(data):
    global linear_velocity, angular_velocity, msg
    
    rospy.loginfo("Joystick Data (Axes): %s", data.axes)
    rospy.loginfo("Joystick Data Length: %d", len(data.axes))

    # Assuming axis 1 controls forward/backward movement and axis 0 controls rotation
    # Modify these indices based on your joystick setup
    linear_velocity = data.axes[1] * 5 # Forward/backward control (usually axis 1)
    angular_velocity = data.axes[3] * 5 # Left/right rotation control (usually axis 0)

    # Set the linear and angular velocities
    msg.linear.x = linear_velocity
    msg.angular.z = angular_velocity

# Main function to initialize ROS node and subscribe to the joystick
if __name__ == "__main__":
    rospy.init_node("controller")
    rospy.loginfo("Controller node started")

    pub = rospy.Publisher("/RosAria/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber("joy", Joy, joy_callback)
    rate = rospy.Rate(10)  # 10 Hz rate for publishing the messages

    while not rospy.is_shutdown():
        # Publish the current velocities
        pub.publish(msg)
        rate.sleep()
