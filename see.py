import rospy
import cv2
from sensor_msgs.msg import Image

from cv_bridge import CvBridge, CvBridgeError

if __name__ == "__main__":
    cam_id = input("camera id : ")
    rospy.init_node('see', anonymous=True)
    pub = rospy.Publisher('/camera/image', Image, queue_size=10)
    cap = cv2.VideoCapture(cam_id)
    rate = rospy.Rate(10)
    try:
        while not rospy.is_shutdown():
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bridge = CvBridge()
            img_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(img_msg)
            rate.sleep()    
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break
        cap.release();
        cv2.destroyAllWindows()  
    except rospy.ROSInterruptException:
        pass
    
 
