import re
from typing import List

from ..event import Event
from ..source import Source


class AccaddeOggi(Source):
    URL = "https://www.accaddeoggi.it"

    def parse(self) -> List[Event]:
        soup = self.get_soup(self.URL)

        stop_tag = soup.find(text="Sono nati oggi")

        event_list = stop_tag.find_all_previous("div", class_="entry")

        res = []
        for event in event_list:
            text = event.find("a").text
            text = text.replace("&nbsp;", "")

            year, title = re.split("-|–", text, maxsplit=1)
            res.append(self.to_event(year, title))

        res.reverse()

        return res
