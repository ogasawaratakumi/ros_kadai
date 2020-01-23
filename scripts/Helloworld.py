#!/usr/bin/env python

import rospy
from std_msgs.msg import String
kawa = ' Kawa'
world = ' World'

rospy.init_node( 'HelloWorld' )
pub = rospy.Publisher( 'Helloworld', String, queue_size=1 )
rate = rospy.Rate(1)

def cb( message ):
	if 'Y' in message.data:
	  msg = message.data + kawa
	else:
	  msg = message.data + world
	pub.publish(msg)

if __name__ == '__main__':
   sub = rospy.Subscriber( 'word', String, cb )
   while not rospy.is_shutdown():
	 rate.sleep()
