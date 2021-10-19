# onthisday

Simple library that retrieves the historical events that happened on current day.

At the moment the events do not include birth/death of famous people.

## Event sources
- [Italian Wikipedia](https://it.wikipedia.org/wiki/Oggi) 🇮🇹
- [Accadde Oggi](https://www.accaddeoggi.it/) 🇮🇹

## Install
...

## Usage

### As a standalone script
In the root directory:

```angular2html
> python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Commands:
  all     Print all the events of today
  last    Print last n events of today
  list    List the available sources (valid shorter names in brackets)
  random  Print random event of today
```

For the specific command options:

```angular2html
> python main.py all --help

Usage: main.py all [OPTIONS]

  Print all the events of today

Options:
  --source TEXT  [default: wiki]
  --help         Show this message and exit.

```

### As a library
_see the [example file](example.py) provided_ 

## Issues
Please open issue on this Github repository for any error, suggestion or feature request.