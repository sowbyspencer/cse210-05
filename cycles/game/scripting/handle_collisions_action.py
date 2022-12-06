import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    
    def _handle_segment_collision(self, cast):
        """If the head of one cycle collides with the head of the other cycle or the segments of the other
        cycle, then the game is over
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # The above code is getting the actors from the cast and assigning them to variables.
        scores = cast.get_actors("scores")
        score1 = scores[0]
        score2 = scores[1]
        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        head1 = cycle1.get_segments()[0]
        head2 = cycle2.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        segments2 = cycle2.get_segments()[1:]
        
        # This is checking if the head of the cycle is colliding with the head of the other cycle or
        # the segments of the other cycle. If it is, then the game is over.
        if head1.get_position().equals(head2.get_position()):
            self._is_game_over = not self._is_game_over

        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                score1.add_points(1)
                self._is_game_over = not self._is_game_over

        for segment in segments2:
            if head1.get_position().equals(segment.get_position()):
                score2.add_points(1)
                self._is_game_over = not self._is_game_over

        if len(segments1) == 0 or len(segments2) == 0:
            self._is_game_over = not self._is_game_over

        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            # Creating a message that says "Game Over!" and then it is changing the color of the
            # cycles to white.
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            cycles = cast.get_actors("cycles")

            for cycle in cycles:
                segments = cycle.get_segments()
                for segment in segments:
                    segment.set_color(constants.WHITE)