from bs4 import BeautifulSoup
from onthisday.sources.accadde_oggi import AccaddeOggi


def test_parse(mocker, events):

    def load_html(*_) -> BeautifulSoup:
        return BeautifulSoup(
            open("tests/sources/accadde_oggi/accadde_oggi.html"),
            "html.parser"
        )

    mocker.patch('onthisday.source.Source.get_soup', load_html)

    a = AccaddeOggi()
    actual = a.parse()

    assert len(actual) == len(events)

    for idx in range(len(actual)):
        assert actual[idx].year == events[idx].year
        # TODO compare titles
