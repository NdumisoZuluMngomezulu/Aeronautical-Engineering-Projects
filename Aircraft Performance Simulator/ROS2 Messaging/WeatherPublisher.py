import rclpy

from rclpy.node import Node

from std_msgs.msg import Float32

class WeatherNode(Node):

    def __init__(self):

        super().__init__(
            'weather_node'
        )

        self.publisher = (
            self.create_publisher(
                Float32,
                'wind_speed',
                10
            )
        )

        self.timer = (
            self.create_timer(
                1.0,
                self.publish_weather
            )
        )

    def publish_weather(self):

        msg = Float32()

        msg.data = 12.5

        self.publisher.publish(msg)