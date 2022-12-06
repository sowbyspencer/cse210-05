from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here!

class MoveActorsAction(Action):

    # Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        """
        Loop through all the actors in the cast and call the move_next() method on each one.
        
        :param cast: the cast of actors
        :param script: the script that the cast is performing
        """
        # 1) get all the actors from the cast
        actors = cast.get_all_actors()
        # 2) loop through the actors
        for actor in actors:
            # 3) call the move_next() method on each actor
            actor.move_next()