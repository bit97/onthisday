import pytest
from onthisday.event import Event
from onthisday.source import Source
from bs4 import BeautifulSoup
from urllib import request


@pytest.fixture
def event():
    return Event(2006, "Italy wins world cup", False)


@pytest.mark.parametrize('year', [' 2006  ', '2006', '2006 some garbage'])
def test_to_event(event, year):
    e = Source.to_event(year, "    Italy wins world cup ")

    assert e == event


@pytest.mark.parametrize('year,error', [
    (2006, AttributeError),
    (1920.5, AttributeError),
    ('invalid 2006', ValueError)
])
def test_to_event_invalid_conversion(year, error):
    with pytest.raises(error):
        Source.to_event(year, "Dummy title")


WIKI_URL = "https://it.wikipedia.org/wiki/Oggi"


@pytest.fixture(scope='module')
def wiki():
    with request.urlopen(WIKI_URL) as body:  # skipcq: BAN-B310
        return BeautifulSoup(body, "html.parser")


def test_get_soup(wiki):
    # Allow instantiation of abstract class
    Source.__abstractmethods__ = {}
    s = Source()

    assert s.get_soup(WIKI_URL) == wiki


@pytest.mark.parametrize('protocol', ['http', 'ftp', 'smb', 'file'])
def test_get_soup_url_incorrect(wiki, protocol):
    # Allow instantiation of abstract class
    Source.__abstractmethods__ = {}
    s = Source()

    url = WIKI_URL.replace("https", protocol)

    with pytest.raises(ValueError):
        s.get_soup(url)


def test_validate_url():
    assert Source._validate_url('https://www.example.com/')


@pytest.mark.parametrize('protocol', ['http', 'ftp', 'smb', 'file'])
def test_validate_url_incorrect(protocol):
    assert not Source._validate_url(f'{protocol}://www.example.com/')
