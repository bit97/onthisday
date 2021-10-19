from typing import Optional

from typer import Typer
from onthisday import Today

app = Typer()


@app.command(name='all')
def all_(source: str = 'wiki') -> None:
    """Print all the events of today"""
    event_source = Today(source)
    print(*event_source.all(), sep="\n")


@app.command(name='last')
def last_(n: int = 1, source: str = 'wiki', from_year: Optional[str] = None, to_year: Optional[str] = None) -> None:
    """Print last n events of today"""
    event_source = Today(source)
    print(*event_source.last(n, from_year=from_year, to_year=to_year), sep="\n")


@app.command(name='random')
def random_(source: str = 'wiki', from_year: Optional[str] = None, to_year: Optional[str] = None) -> None:
    """Print random event of today"""
    event_source = Today(source)
    print(event_source.random(from_year=from_year, to_year=to_year))


@app.command(name='list')
def list_() -> None:
    """List the available sources (valid shorter names in brackets)"""
    available_sources = ['Wikipedia (wiki)', 'Accadde Oggi (accadde)']
    print(f'\nAvailable sources:\n')

    for source in available_sources:
        print(f'    • {source}')


# Launch as a standalone script
if __name__ == '__main__':
    app()
