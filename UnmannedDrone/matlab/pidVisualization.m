kp = 1.2;
ki = 0.5;
kd = 0.2;

sys = tf([1], [1 10 20]);

controller = pid(kp, ki, kd);

closed_loop = feedback(controller * sys, 1);

step(closed_loop)

title('PID Controlled Drone Response')