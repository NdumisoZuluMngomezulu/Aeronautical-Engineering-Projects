class AircraftNode(Node):

    def __init__(self):

        super().__init__(
            'aircraft_node'
        )

        self.subscription = (
            self.create_subscription(
                Float32,
                'wind_speed',
                self.wind_callback,
                10
            )
        )

    def wind_callback(self, msg):

        self.wind_speed = msg.data

        print(
            f"Wind = {self.wind_speed}"
        )