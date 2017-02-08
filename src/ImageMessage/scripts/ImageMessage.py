#!/usr/bin/env python

import numpy as np
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageMessage:
    def __init__(self):
        self.im_pub = rospy.Publisher("img_message", Image, queue_size=1)
        self.bridge = CvBridge()
        self.im_sub = rospy.Subscriber('cv_camera/image_raw', Image, self.callback)
        #self.sub = rospy.Subscriber('sentence', str, self.ImageMessage)

    def callback(self, data):
        try:
            img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        Message = "Robot System 2016"
        font = cv2.FONT_HERSHEY_PLAIN
        w,h,channel = img.shape
        pub_img = cv2.putText(img,Message,(w/8,h/8),font, 3,(255,255,0),3)
        
        try:
            self.im_pub.publish(self.bridge.cv2_to_imgmsg(pub_img, "bgr8"))
        except CvBridgeError as e:
            print(e)


if __name__ == '__main__':
    fc = ImageMessage()
    rospy.init_node('Image_message', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    #image = np.zeros((rows, cols, 3), np.uint8)

