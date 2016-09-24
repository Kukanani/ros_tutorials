#!/usr/bin/env python

import sys
import pygame
import rospy
from geometry_msgs.msg import Twist

###########################################################
# pygame
pygame.init()

size = width, height = 100, 100
speed = [2, 2]
black = 0, 0, 0

pygame.display.set_caption("improved teleop")
screen = pygame.display.set_mode(size)

#########################################################
# ros
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
rospy.init_node('improved_teleop', anonymous=True)
rate = rospy.Rate(10)

rot_speed = 1.0
lin_speed = 1.0

#########################################################
# loop
while 1:
    angular_movement = 0
    linear_movement = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        angular_movement = rot_speed

    if keys[pygame.K_RIGHT]:
        angular_movement = -rot_speed

    if keys[pygame.K_UP]:
        linear_movement = lin_speed

    if keys[pygame.K_DOWN]:
        linear_movement = -lin_speed

    twist = Twist()
    twist.angular.z = angular_movement
    twist.linear.x = linear_movement
    pub.publish(twist)
    rate.sleep()