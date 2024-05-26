#!/usr/bin/env python3
import rospy as rp
from geometry_msgs.msg import Twist
import time as t

def move_square():
    rp.init_node('move_square', anonymous=True)
    pub = rp.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rp.Rate(1)  
    move_cmd = Twist()
    linear_speed = 0.33
    angular_speed = 1
    straight_time = 2
    turn_time = 1.571
    
    while not rp.is_shutdown():
        for _ in range(4):
            # move st
            move_cmd.linear.x = linear_speed
            move_cmd.angular.z = 0
            pub.publish(move_cmd)
            t.sleep(straight_time)
            
            # stop
            move_cmd.linear.x = 0
            move_cmd.angular.z = 0
            pub.publish(move_cmd)
            t.sleep(1)
            
            # turn 90 deg
            move_cmd.linear.x = 0
            move_cmd.angular.z = angular_speed
            pub.publish(move_cmd)
            t.sleep(turn_time)
            
            # stop
            move_cmd.linear.x = 0
            move_cmd.angular.z = 0
            pub.publish(move_cmd)
            t.sleep(1)

if __name__ == '__main__':
    try:
        move_square()
    except rp.ROSInterruptException:
        pass
