class PIDController {
private:
    double kp;
    double ki;
    double kd;

    double previousError;
    double integral;

public:
    PIDController(double p, double i, double d)
        : kp(p), ki(i), kd(d), previousError(0), integral(0) {}

    double calculate(double setpoint, double measured) {
        double error = setpoint - measured;

        integral += error;

        double derivative = error - previousError;

        previousError = error;

        return kp * error + ki * integral + kd * derivative;
    }
};