"""
  853. Car Fleet
  [ Medium ] | [ 50.2% ] -- Solved 12/02/2023 -- [ Sorting, Monotonic Stack ]

  Problem Statement:
  - There are n cars going along a one-way road, cars can't overtake, so when a faster car catches up to a slower one,
    it slows down to match the speed of the faster car at the same position
  - A speed and pos array are given for the n cars
  - Find the number of fleets (groups o cars) that pass the finish line at the same position

  Approach:
  - Since overtaking isn't allowed, the car immediately ahead impacts the run of the car being considered
  - Hence, we need to consider each car in order of its starting position
  - The idea needed to solve this problem is that if car 1 takes longer to reach the destination than the cars behind
    it if overtaking was allowed, then the cars behind that would have been faster otherwise, are limited by the car
    in front of them and will reach the destination at the same time as the car in front
  - Example: Let's say the array below represents the times each car would take to arrive at target if overtaking was
    allowed, and the cars are in order of position
  - [10, 2, 5, 7, 15, 12, 20, 17] - then..
    - [10, 2, 5, 7] is fleet 1, since the latter 3 cars will reach the first car and won't be able to overtake it
    - [15, 12] and [20, 17] are the second and third fleets according to the same principle

  - Sort the input arrays so that positions are in descending order
  - Essentially just need to keep track of how many times the minimum of the time to target is updated
  - Cars which cause that minimum to be updated are at the head of the fleet, the others are the ones that eventually
    hit the head of the fleet and have to slow down

  MONOTONIC STACK
  - This can be modelled by a monotonic stack by calculating time to target in the same sorted order and pushing it to
    a monotonically increasing stack
  - As soon as a greater value is encountered, it wipes out the smaller values towards the top of the stack

  Time Complexity: O(NlogN)
  Space Complexity: O(N)
"""

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pairs = sorted(zip(position, speed), reverse=True)
    slowest = -1
    fleets = 0
    for pos, s in pairs:
        ttd = (target - pos) / s
        if ttd > slowest:
            fleets += 1
            slowest = ttd
    return fleets