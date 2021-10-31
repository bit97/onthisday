from abc import ABC, abstractmethod
from datetime import date
from typing import List
from urllib import request

from bs4 import BeautifulSoup

from .event import Event


class Source(ABC):
    """
    Abstract Source class. Classes that will derive from this will
    have to implement abstract method and provide a parsing of the webpage
    """

    def __init__(self) -> None:
        """Construct an abstract source class"""
        self.today = date.today()

    @abstractmethod
    def parse(self) -> List[Event]:
        """Interface method that allow parsing of events"""

    @staticmethod
    def to_event(year: str, title: str, bc: bool = False) -> Event:
        """Creates an event based on its string representation"""
        return Event(int(year.split()[0]), title.strip(), bc)

    def get_soup(self, url: str) -> BeautifulSoup:
        """Returns an instance of BeautifulSoup parser. Raise an exception on insecure URL"""
        if not self._validate_url(url):
            raise ValueError("Not going to get resource from unsecure URL")

        req = request.Request(url)
        with request.urlopen(req) as body:  # skipcq: BAN-B310
            return BeautifulSoup(body, "html.parser")

    @staticmethod
    def _validate_url(url: str) -> bool:
        """Validate URL by only allowing secure connections"""
        return url.lower().startswith("https")
