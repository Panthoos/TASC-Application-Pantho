#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String   # message type
from tasc_application import rover_data as rd

class DataPublisher(Node):
    def __init__(self):
        super().__init__("rover_data_publisher")  
        # publisher: sends messages of type String
        self.publisher = self.create_publisher(String, "rover_data_topic", 10)  
        self.timer = self.create_timer(1.0, self.publish_data)  
        self.get_logger().info("PUBLISHING DATA . . .")

    def publish_data(self):
        msg = String()
        msg.data = (f"GPS: {rd.gps}\n"
                    f"Battery: {rd.battery[0]}%\n"
                    f"Sensor Distance: {rd.sensors[0]}m\n"
                    f"Internal Temp: {rd.sensors[1]}℃, External Temp: {rd.sensors[2]}℃\n"
                    f"Signal Strength: {rd.comstrength[0]} dBm\n"
                    f"Motor Feedback - Commanded: {rd.motorfeedback[0]} m/s, Measured: {rd.motorfeedback[1]}m/s \n\n"
            )
        
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DataPublisher()
    rclpy.spin(node)   # keep running until stopped
    rclpy.shutdown()

if __name__ == "__main__":
    main()