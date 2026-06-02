class Weather:

    def __init__(
        self,
        temperature,
        pressure,
        humidity,
        wind_speed,
        wind_direction
    ):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def air_density(self):

        temp_k = self.temperature + 273.15

        R = 287.05

        rho = self.pressure / (R * temp_k)

        return rho