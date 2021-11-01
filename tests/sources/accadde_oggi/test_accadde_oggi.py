import pytest
from bs4 import BeautifulSoup
from urllib import request
import os
from onthisday.sources.accadde_oggi import AccaddeOggi


def test_parse(mocker, events):
    def load_html(self_unused, url_unused) -> BeautifulSoup:
        path = os.path.abspath("sources/accadde_oggi/accadde_oggi.html")
        req = request.Request(f'file://{path}')
        with request.urlopen(req) as body:  # skipcq: BAN-B310
            return BeautifulSoup(body, "html.parser")

    mocker.patch('onthisday.source.Source.get_soup', load_html)

    a = AccaddeOggi()
    actual = a.parse()

    # TODO enable test

    #assert len(actual) == len(events)

    for idx in range(len(actual)):
        #assert actual[idx].year == events[idx].year
        #assert actual[idx].title == events[idx].title
        pass
