from random import choice
from typing import List

from .event import Event
from .sources import AccaddeOggi, Wikipedia


class Today:
    """Interface class that provides information about events."""

    def __init__(self, source_name: str = "wiki", locale: str = None) -> None:
        source_name = source_name.lower()
        if "wiki" in source_name:
            self.source = Wikipedia(locale)
        elif "accadde" in source_name:
            self.source = AccaddeOggi()
        else:
            raise NotImplementedError(f"Unsupported source type {source_name}")

    def _retrieve(self, **kwargs) -> List[Event]:
        """Parse the events and retrieve them, eventually filtered based on passed arguments"""
        events = self.source.parse()

        if "from_year" in kwargs and kwargs["from_year"]:
            events = [
                event
                for event in events
                if event.get_year() >= int(kwargs["from_year"])
            ]

        if "to_year" in kwargs and kwargs["to_year"]:
            events = [
                event for event in events if event.get_year() <= int(kwargs["to_year"])
            ]

        return events

    def last(self, n: int = 1, **kwargs) -> List[Event]:
        """Returns the last *n* events, without affecting the order"""
        events = self._retrieve(**kwargs)
        return events[slice(abs(n) * -1, None)]

    def random(self, **kwargs) -> Event:
        """Returns a single random event"""
        events = self._retrieve(**kwargs)

        return choice(events)

    def all(self) -> List[Event]:
        """Return all the events, without affecting the order"""
        return self._retrieve()
