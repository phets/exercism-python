"""
Module to solve the space-age exercise from exercism.org.
https://exercism.org/tracks/python/exercises/space-age
"""
class SpaceAge:
    """
    The exercise requires creation of the SpaceAge class.
    """
    # A list of tuples containing the planets and their 
    # orbital period in seconds.
    ORBIT_SECONDS = [
        (planet, orbital_period * 31557600)
        for planet, orbital_period in (
            ('mercury', 0.2408467),
            ('venus', 0.61519726),
            ('earth', 1.0),
            ('mars', 1.8808158),
            ('jupiter', 11.862615),
            ('saturn', 29.447498),
            ('uranus', 84.016846),
            ('neptune', 164.79132)
        )
    ]
    
    def __init__(self, seconds: int):
        """
        The constructor initializes the age_in_seconds instance variable
        and then creates a function called on_<planet_name> for each
        planet in the ORBIT_SECONDS list.

        Args:
            seconds (int): The number of seconds to transfor in planet years.
        """
        self.age_in_seconds = seconds
    
        for planet, orbital_period in self.ORBIT_SECONDS:
            # setattr adds "attributes", in this case functions, to the class.
            setattr(
                self,
                f'on_{planet}',
                lambda orbital_period = orbital_period: round(self.age_in_seconds / orbital_period, 2 )
            )
