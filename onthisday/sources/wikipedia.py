import re
from typing import List, Optional, Tuple

from babel.dates import format_date

from ..event import Event
from ..source import Source


class Wikipedia(Source):
    """
    Source derived class for Wikipedia's today articles.
    Support for multiple languages
    """

    DEFAULT_LOCALE = "en"

    def __init__(self, locale: str = None) -> None:
        super().__init__()
        self.locale = locale or Wikipedia.DEFAULT_LOCALE

    @staticmethod
    def _remove_tags(text: str) -> str:
        """Utility to remove text contained in square brackets"""
        return re.sub(r"\[\d+]", "", text)

    def _sanitize(self, year: str, title: str) -> Tuple[str, str, Optional[bool]]:
        """Utility to return a tuple ready to be converted into an Event"""
        title = self._remove_tags(title)

        if "a.C." in year:
            year = re.sub(r"a\.C\.", "", year)
            return year, title, True

        return year, title

    def _build_date(self, locale: str) -> str:
        """
        Build the date portion of the URL, eventually operating on the representation of the day if the
        locale requires it
        """
        date = format_date(self.today, "d_MMMM", locale=self.locale)

        # Handle exceptions
        if locale in ("es", "pt"):
            idx = date.find("_")
            date = date[:idx] + "_de" + date[idx:]
        elif locale == "de":
            idx = date.find("_")
            date = date[:idx] + "." + date[idx:]

        return date

    def _build_url(self) -> str:
        """Build the URL to download the events from"""
        day = self._build_date(self.locale)

        return f"https://{self.locale}.wikipedia.org/wiki/{day}"

    def parse(self) -> List[Event]:
        """Implementation of the abstract method"""
        url = self._build_url()
        soup = self.get_soup(url)

        # Retrieve "Events" h2 tag
        starting_tag = soup.findAll("h2")[1]

        # Limit the research to "Events" tag only, i.e. stop at the next h2 tag
        ending_tag = starting_tag.find_next_sibling("h2")

        # Complete list of siblings tags of "Events" h2 tag, we'll stop at ending_tag
        siblings = starting_tag.next_siblings

        event_list = []

        for tag in siblings:

            if tag == ending_tag:
                break

            # Find all the lists in the "Events" tag and populate the event_list
            # with <li> elements
            if tag.name == "ul":
                event_list.extend(tag.find_all("li", recursive=False))

        raw_events = []

        for event in event_list:

            if subevents := event.find("ul"):
                # Multiline event
                year = event.a.text
                for subevent in subevents.find_all("li"):
                    title = subevent.text
                    raw_events.append((year, title))
            elif event.text.strip() != "":
                # Simple event
                try:
                    year, title = re.split("-|–|—|:|ː", event.text, maxsplit=1)
                except ValueError:
                    pass
                raw_events.append((year, title))

        return [self.to_event(*self._sanitize(*raw)) for raw in raw_events]
