from dataclasses import dataclass


@dataclass
class Event:
    """
    Simple class for representing an event, characterized by a year (eventually BC)
    and a title
    """

    year: int
    title: str
    bc: bool = False

    def __str__(self) -> str:
        """String representation of the event"""
        return f'[{self.year}{" a.C." if self.bc else ""}] ' f"{self.title}"

    def get_year(self) -> int:
        """Getter for the event's year. BC dates are expressed by negative values"""
        return self.year if not self.bc else -self.year
