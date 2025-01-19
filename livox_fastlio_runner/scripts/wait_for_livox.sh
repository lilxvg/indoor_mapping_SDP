#!/bin/bash

# Start the Livox driver
roslaunch livox_ros_driver2 msg_MID360.launch &
sleep 5  # Wait 


while ! rostopic list | grep -q "/livox/lidar"; do
    echo "Waiting for Livox lidar topic..."
    sleep 1
done


roslaunch fast_lio mapping_mid360.launch
