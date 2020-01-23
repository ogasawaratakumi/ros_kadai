#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import String

rospy.init_node( 'word' )
pub = rospy.Publisher( 'word', String, queue_size=1 )
rate = rospy.Rate(1)

while not rospy.is_shutdown():
  x = random.randint( 1, 5 )
  if x == 2:
    w = 'Yama'
  else:
    w = 'Hello'
  pub.publish(w)
  rate.sleep()
