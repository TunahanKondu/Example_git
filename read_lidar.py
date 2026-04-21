import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class ScanToTextOverwrite(Node):
    def __init__(self):
        super().__init__('scan_to_text_overwrite_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)
        
        self.filename = "lidar_current_scan.txt"
        self.get_logger().info(f"Monitoring /scan. Latest data is being written to {self.filename}")

    def listener_callback(self, msg):
        # Using "w" mode deletes the old content and writes fresh data
        with open(self.filename, "w") as f:
            f.write(f"Timestamp: {msg.header.stamp.sec}.{msg.header.stamp.nanosec}\n")
            f.write(f"Points in scan: {len(msg.ranges)}\n")
            f.write(f"{'Index':<10} | {'Angle (deg)':<15} | {'Range (m)':<10}\n")
            f.write("-" * 40 + "\n")

            for i, distance in enumerate(msg.ranges):
                # Calculate angle for this index
                angle_deg = math.degrees(msg.angle_min + (i * msg.angle_increment))
                
                # Write the row
                f.write(f"{i:<10} | {angle_deg:<15.2f} | {distance:<10.3f}\n")
            
        # Optional: Use a debug log so you know it's working
        # self.get_logger().info("File updated with latest scan.")

def main(args=None):
    rclpy.init(args=args)
    node = ScanToTextOverwrite()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
