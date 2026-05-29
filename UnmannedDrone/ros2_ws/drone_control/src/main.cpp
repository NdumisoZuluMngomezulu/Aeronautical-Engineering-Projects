#include <chrono>
#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

using namespace std::chrono_literals;

class DronePublisher : public rclcpp::Node {
public:
    DronePublisher() : Node("drone_publisher") {
        publisher_ = this->create_publisher<std_msgs::msg::String>("drone/status", 10);
        
        // Fixed: create_wall_timer takes 2 arguments: duration and callback function
        timer_ = this->create_wall_timer(
            1000ms, 
            std::bind(&DronePublisher::publishStatus, this)
        );
    }

private:
    void publishStatus() {
        auto message = std_msgs::msg::String();
        message.data = "Drone is stable";
        
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
        publisher_->publish(message);
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<DronePublisher>());
    rclcpp::shutdown();
    return 0;
}



