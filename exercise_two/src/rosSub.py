#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
a= 't'
b=0
c=0
def callback(data):
	x= data.data.split(",")
	name= x[0].split()
	age= x[1].split()
	height= x[2].split()
	a=name[1]
	c=int(age[1])
	b=int(height[1])
	rospy.loginfo(a)
	rospy.loginfo(c)
	rospy.loginfo(b)
	pub = rospy.Publisher('/name', String, queue_size=10)
	pubage = rospy.Publisher('/age', Int32, queue_size=10)
	pubheight = rospy.Publisher('/height', Int32, queue_size=10)
	pub.publish(a)
	pubage.publish(c)
	pubheight.publish(b)
	rate = rospy.Rate(1)
	rate.sleep()


def listener() :
	rospy.init_node('data_processing', anonymous=True)
	rospy.Subscriber("/raw_data", String, callback)
	rospy.spin()
	
	
if __name__== '__main__' :
	listener()
