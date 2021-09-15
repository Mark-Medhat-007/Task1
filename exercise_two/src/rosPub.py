#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String 

def talker():
	pub = rospy.Publisher('/raw_data', String, queue_size=10)
	
	rospy.init_node('user_info_driver', anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():

		name = input ("Enter name :")
		age= input ("Enter age :")
		height= input ("Enter height :")
		rospy.loginfo(name)
		rospy.loginfo(age)
		rospy.loginfo(height)
		x="Name= %s,age= %s, height= %s" %(name, age, height)
		rospy.loginfo(x)
		pub.publish(x)
		rate.sleep()
		
if __name__==  '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
