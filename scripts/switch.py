#!/usr/bin/env python
#encoding: utf8
import sys, rospy
from std_srvs.srv import Trigger, TriggerResponse

if __name__ == '__main__':

  rospy.init_node('switch_motors')
  srv_on_switch = rospy.ServiceProxy('motor_on', Trigger)
  srv_off_swicth = rospy.ServiceProxy('motor_off', Trigger)

  rate = rospy.Rate(5)
  count_bef = '1\n' 
  count_aft = '1\n'
  count = 1
  while not rospy.is_shutdown():
    try:
      with open('/dev/rtswitch2','r') as f:

        count_bef=count_aft

        rate.sleep()
        switch=f.readline()

        count_aft=switch

        if(count_bef=='1\n' and count_aft=='0\n'):
          if(count>0):
            srv_on_switch()
            count=-1*count
          else:
            srv_off_swicth()
            count=-1*count

    except rospy.ServiceException, e:
      print "Service call failed: %s"%e
        





