clc;
clear;

x = 0:0.1:10;
altitude = sin(x) + 5;

plot(x, altitude)

xlabel('Time')
ylabel('Altitude')
title('Drone Altitude Simulation')
grid on