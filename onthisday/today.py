from random import choice
from typing import List
from .event import Event
from .source import Wikipedia, AccaddeOggi


class Today:
    def __init__(self, source_name: str = 'wiki') -> None:
        source_name = source_name.lower()
        if 'wiki' in source_name:
            self.source = Wikipedia()
        elif 'accadde' in source_name:
            self.source = AccaddeOggi()
        else:
            raise NotImplementedError(f'Unsupported source type {source_name}')

    def _retrieve(self, **kwargs) -> List[Event]:
        events = self.source.parse()

        if 'from_year' in kwargs and kwargs['from_year']:
            events = [event for event in events if event.get_year() >= int(kwargs['from_year'])]

        if 'to_year' in kwargs and kwargs['to_year']:
            events = [event for event in events if event.get_year() <= int(kwargs['to_year'])]

        return events

    def last(self, n: int = 1, **kwargs) -> List[Event]:
        events = self._retrieve(**kwargs)
        return events[slice(abs(n) * -1, None)]

    def random(self, **kwargs) -> Event:
        events = self._retrieve(**kwargs)

        return choice(events)

    def all(self) -> List[Event]:
        return self._retrieve()
