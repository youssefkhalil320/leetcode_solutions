from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of position and speed, then sort based on position in descending order
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        time_to_reach = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            # If the time for the current car to reach the target is greater than the
            # time of the previous car, it forms a new fleet
            if time > time_to_reach:
                fleets += 1
                time_to_reach = time

        return fleets
