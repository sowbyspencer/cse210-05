import constants
from game.casting.actor import Actor
from game.shared.point import Point


class cycle(Actor):
    """
    The responsibility of cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player):
        super().__init__()
        self._player = player
        self._color = constants.WHITE

        if self._player == 1:
            self._color = constants.GREEN
        else:
            self._color = constants.RED
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """
        It returns the segments of the line.
        :return: The segments of the line.
        """
        return self._segments

    def move_next(self):
        """
        The function moves all the segments of the snake and updates the velocities of the segments
        """
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """
        It returns the first element of the list.
        :return: The head of the snake.
        """
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """
        It checks if the cycle is white or not. If it is white, it will set the color to white. If it is
        not white, it will set the color to green
        
        :param number_of_segments: This is the number of segments that will be added to the tail
        """

        # This is checking if the cycle is white or not. If it is white, it will set the color to
        # white. If it is not white, it will set the color to green.
        if len(self._segments) > 0:
            if self._segments[0].get_color() == constants.WHITE:
                self._color = constants.WHITE
            else:
                for i in range(number_of_segments):
                    tail = self._segments[-1]
                    velocity = tail.get_velocity()
                    offset = velocity.reverse()
                    position = tail.get_position().add(offset)
                    
                    segment = Actor()
                    segment.set_position(position)
                    segment.set_velocity(velocity)
                    segment.set_text("#")
                    segment.set_color(self._color)

                    self._segments.append(segment)

    def turn_head(self, velocity):
        """
        The function turn_head() takes in a velocity and sets the velocity of the head segment to that
        velocity
        
        :param velocity: The velocity of the head
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """
        > The function creates a snake with a length of 8, with the head in the middle of the screen,
        and the body segments following behind
        """

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        if self._player == 1:
            x = int(2*constants.MAX_X / 2 )
        else:
            x = int((constants.MAX_X / 2))

        
        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else self._color
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)