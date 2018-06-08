#/usr/bin/python

import rospy
import numpy as np
import math
import mavros_msgs

from geometry_msgs.msg import PoseStamped
from mavros_msgs import srv
from mavros_msgs.msg import State



class Quad(object):
	def __init__(self):
		self.current_pose = PoseStamped()
		self.goal_pose = PoseStamped()
		self.wand_pose = [0,0,0]

	def goal_pose_update()
		
	





quad = Quad()
rospy.init_node('Offboard_Wand_Follow', anonymous = True)
rate = rospy.Rate(20)

local_position_subscribe = rospy.Subscriber('/Wand',PoseStamped,pos_sub_callback)
local_position_pub = rospy.Publisher('/mavros/setpoint_position/local',PoseStamped,queue_size = 20)

while not rospy.is_shutdown():
	quad.goal_pose_update()

	local_position_pub.publish(quad.goal_pose)

	rate.sleep()






























































