#ifndef DRONE_HPP
#define DRONE_HPP

class Drone {
private:
    double x;
    double y;
    double z;
    double yaw;

    double velocity;

public:
    Drone();

    void takeOff();
    void land();

    void moveForward(double distance);
    void moveBackward(double distance);

    void rotateLeft(double angle);
    void rotateRight(double angle);

    void changeAltitude(double amount);

    void printStatus() const;

    double getAltitude() const;
};