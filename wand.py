#/usr/bin/python

import rospy
import numpy as np
import math
import mavros_msgs

from geometry_msgs.msg import PoseStamped
from mavros_msgs import srv
from mavros_msgs.msg import State



class Wand(object):

	def __init__(self)
		self.m1_pose = [0,0,0]
		self.m2_pose = [0,0,0]
		









wand = Wand()

local_position_subscribe = rospy.Subscriber('/mavros/mocap/pose', PoseStamped, pos_sub_callback)
local_position_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size = 20)

while not rospy.is_shutdown():




















































