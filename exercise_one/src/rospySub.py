#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
	x= data.data.split(",")
	name= x[0].split()
	age= x[1].split()
	height= x[2].split()
	c=int(age[1])
	b=int(height[1])
	rospy.loginfo(name[1])
	rospy.loginfo(c)
	rospy.loginfo(b)



def listener() :
	rospy.init_node('data_processing', anonymous=True)
	rospy.Subscriber("/raw_data", String, callback)
	rospy.spin()
	
if __name__== '__main__' :
	listener()
