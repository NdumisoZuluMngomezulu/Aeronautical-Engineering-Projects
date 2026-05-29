#include <iostream>
#include "Drone.hpp"

Drone::Drone() {
    x = 0;
    y = 0;
    z = 0;
    yaw = 0;
    velocity = 1.0;
}

void Drone::takeOff() {
    z = 1.0;
    std::cout << "Drone taking off..." << std::endl;
}

void Drone::land() {
    z = 0;
    std::cout << "Drone landing..." << std::endl;
}

void Drone::moveForward(double distance) {
    x += distance;
}

void Drone::moveBackward(double distance) {
    x -= distance;
}

void Drone::rotateLeft(double angle) {
    yaw -= angle;
}

void Drone::rotateRight(double angle) {
    yaw += angle;
}

void Drone::changeAltitude(double amount) {
    z += amount;
}

void Drone::printStatus() const {
    std::cout << "Position: ("
              << x << ", "
              << y << ", "
              << z << ")"
              << std::endl;

    std::cout << "Yaw: " << yaw << std::endl;
}

double Drone::getAltitude() const {
    return z;
}