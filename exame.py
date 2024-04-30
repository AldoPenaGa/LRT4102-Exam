#!/usr/bin/env python3
import rospy
import random
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill
import sys
import termios
import tty
import select

class TurtleChase:
    def __init__(self):
        rospy.init_node('turtle_chase')
        self.vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        
        self.turtle1_pose = Pose()
        self.target_pose = Pose()
        self.is_target_alive = False
        
        self.settings = termios.tcgetattr(sys.stdin)
        self.spawn_turtle = rospy.ServiceProxy('spawn', Spawn)
        self.kill_turtle = rospy.ServiceProxy('kill', Kill)

        # PID coefficients
        self.Kp_linear = 1.0
        self.Ki_linear = 0.01
        self.Kd_linear = 0.05
        self.Kp_angular = 4.0
        self.Ki_angular = 0.02
        self.Kd_angular = 0.1

        # Error terms for PID
        self.linear_integral = 0.0
        self.angular_integral = 0.0
        self.prev_linear_error = 0.0
        self.prev_angular_error = 0.0

    def update_pose(self, data):
        self.turtle1_pose = data

    def spawn_target(self):
        if not self.is_target_alive:
            self.target_pose.x = random.uniform(2, 10)
            self.target_pose.y = random.uniform(2, 10)
            self.spawn_turtle(self.target_pose.x, self.target_pose.y, 0, 'turtle2')
            self.is_target_alive = True
            

    def kill_target(self):
        self.kill_turtle('turtle2')
        self.is_target_alive = False

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def calculate_pid(self, error, prev_error, integral, Kp, Ki, Kd):
        integral += error
        derivative = error - prev_error
        return Kp * error + Ki * integral + Kd * derivative, integral

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.spawn_target()
            while self.is_target_alive:
                distance = math.sqrt((self.turtle1_pose.x - self.target_pose.x) ** 2 + (self.turtle1_pose.y - self.target_pose.y) ** 2)
                angle_to_target = math.atan2(self.target_pose.y - self.turtle1_pose.y, self.target_pose.x - self.turtle1_pose.x)

                linear_error = distance
                angular_error = angle_to_target - self.turtle1_pose.theta

                vel_linear, self.linear_integral = self.calculate_pid(linear_error, self.prev_linear_error, self.linear_integral, self.Kp_linear, self.Ki_linear, self.Kd_linear)
                vel_angular, self.angular_integral = self.calculate_pid(angular_error, self.prev_angular_error, self.angular_integral, self.Kp_angular, self.Ki_angular, self.Kd_angular)

                self.prev_linear_error = linear_error
                self.prev_angular_error = angular_error

                velocity_msg = Twist()
                velocity_msg.linear.x = max(min(vel_linear, 1.5), 0)  # limit max speed
                velocity_msg.angular.z = vel_angular
                self.vel_publisher.publish(velocity_msg)

                if distance < 0.5:
                    self.kill_target()

                rate.sleep()

            if self.get_key() == 'e':
                print("Stopping the program.")
                break
        

if __name__ == '__main__':
    try:
        chaser = TurtleChase()
        chaser.run()
    except rospy.ROSInterruptException:
        pass
