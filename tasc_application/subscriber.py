#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String   

class DataSubscriber(Node):
    def __init__(self):
        super().__init__("rover_data_subscriber")
        self.data_subscriber = self.create_subscription(String,                
            "rover_data_topic", self.data_callback, 10)
            #listen to rover_data_topic from publisher

    def data_callback(self, msg):
        self.get_logger().info(f"\nReceived rover data:\n{msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = DataSubscriber()
    rclpy.spin(node)   
    rclpy.shutdown()

if __name__ == "__main__":
    main()