import rclpy
import sys
from rclpy.node import Node
from geometry_msgs.msg import Point


class RacingLine(Node):
    def __init__(self) -> None:
        super().__init__("RacingLine")
        self.init_subs()
        self.init_pubs()

    def init_subs(self) -> None:
        #Receive all cones detected after 1 lap, hopefully will have 
        #Receive lap count, such that if it is greater than 1, we can calculate the full racing line otherwise we use the predictive racing line
        pass

    def init_pubs(self) -> None:
        #Publish a track that is a loop, start and finish should be where the lap starts and ends
        pass


    def racing_line_without_car_params(self, cones):
        #Calculates the full racing line without taking the cars specifications into consideration
        #Use delauney mesh for the midpoint, then smooth track and go through length of the track to determine curve and smooth further, relatively cheap
        pass

    def racing_line_with_car_params(self, cones):
        #Calculates the full racing line by taking the cars specifications into consideration
        #Same as without but acceleration, cornering etc are considered in the calculations
        pass

    def predictive_short_racing_line_without_params(self, cones):
        #Calculates a shorter distance racing line without taking the cars specifications into consideration
        #As all tracks are loops, could use a heuristic to predict which direction the track will go based on previous directions
        pass

    def predictive_short_racing_line_with_params(self, cones):
        #Calculates a shorter distance racing line by taking the cars specifications into consideration
        #Does all that the without params does
        pass


def main(args=None) -> None:
    rclpy.init(args=args)

    node = RacingLine()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main(sys.argv)