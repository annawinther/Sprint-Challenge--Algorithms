class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """

        # Start at the beginning and use selection sort to check each item if its smaller than the one the robot is holding. If it's smaller, swap them, and move to the right. 
        # Keep doing this and go over each item until we have a sorted list.
        # In order to swap the items the light needs to be on so the robot can see

        # BROKEN DOWN PSUEDO CODE
        while True:
        # check if the robot is not at the end of the list (as longas he can move to the right, he is good to keep moving to the right)
            # If the robot can no longer move to the right --> I want to make sure that we are at the end of the list and if no swaps were done or the robot goes back to the beginning
            if not self.can_move_right():
                # check to see if the lights are on
                if self.light_is_on():
                    # if so turn them off
                    self.set_light_off()
                    # check to see if he can move left  
                    while self.can_move_left():
                    # as long as he can move to the left, so so to get all the way back to the beginning. 
                        self.move_left()
                # otherwise end 
                else:
                    break

            # if he can move to the right 
            # swap the item with the item at the index he is currecntly at (None). This will also swap None for the item in front.
            self.swap_item()
            # Move to the next item --> to the right
            self.move_right()

            # check and compare the two items. If bigger than the item in front
            # if there is, compare them 
            if self.compare_item() > 0:
                # turn the lights on and swap items
                self.set_light_on()
                # swap if the one he's holding is greater than the one comparing with
                self.swap_item()

            # then move back one step to the left and swap the current item for None 
            self.move_left()
            self.swap_item()
            # then move right and repeat until he has sorted the whole list. 
            self.move_right()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)
    
    robot.sort()
    print(robot._list)