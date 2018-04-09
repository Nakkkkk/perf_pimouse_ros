#!/usr/bin/env python
#encoding: utf8
import sys, rospy
import time
from pimouse_ros.msg import LightSensorValues
from std_msgs.msg import UInt16

class CalcAverage():
  def __init__(self):
    self.count=0
    self.LAV = 0
    self.RAV = 0
#    self.buzzerCount()
#    sub_sensor = rospy.Subscriber('lightsensors', LightSensorValues, self.calc)
#    self.values = LightSensorValues()

  def calc(self, values):
    self.count=self.count+1
    self.LAV += 0
    print "now="+str(self.count)+","+str(values.left_forward)+","+str(values.left_side)+","+str(values.right_side)+","+str(values.right_forward)

  def buzzerCount(self):

    for i in range(2):
      pub_cal.publish(500)
      time.sleep(0.5)
    pub_cal.publish(0)

    time.sleep(0.5)

    for i in range(1):
      pub_cal.publish(500)
      time.sleep(0.5)
    pub_cal.publish(0)

    time.sleep(0.5)
 
    for i in range(1):
      pub_cal.publish(1000)
      time.sleep(0.5)
    pub_cal.publish(0)

if __name__ == '__main__':
  rospy.init_node('calibSensors')
  pub_cal = rospy.Publisher('buzzer', UInt16, queue_size=1)

  c = CalcAverage()
  c.buzzerCount()
  for i in range(1):
    sub_sensor = rospy.Subscriber('lightsensors', LightSensorValues, c.calc)
    c.values = LightSensorValues()
    time.sleep(1)

