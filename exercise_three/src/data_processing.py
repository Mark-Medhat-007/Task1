#!/usr/bin/env python3
import rospy
from exercise_three.msg import UserInfo
from std_msgs.msg import String
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
	pub = rospy.Publisher('/user_info', UserInfo, queue_size=10)
	message=UserInfo()
	message.name=a
	message.age=c
	message.height=b
	rospy.loginfo(message)
	pub.publish(message)
	rate = rospy.Rate(1)
	rate.sleep()


def listener() :
	rospy.init_node('data_processing', anonymous=True)
	rospy.Subscriber("/raw_data", String, callback)
	rospy.spin()
	
	
if __name__== '__main__' :
	listener()
