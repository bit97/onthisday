# onthisday

[![DeepSource](https://deepsource.io/gh/bit97/onthisday.svg/?label=active+issues&token=kFcXBryjHHiGKQ6JebSE3hfw)](https://deepsource.io/gh/bit97/onthisday/?ref=repository-badge)
[![DeepSource](https://deepsource.io/gh/bit97/onthisday.svg/?label=resolved+issues&token=kFcXBryjHHiGKQ6JebSE3hfw)](https://deepsource.io/gh/bit97/onthisday/?ref=repository-badge)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Simple library that retrieves the historical events that happened on current day.

At the moment the events do not include birth/death of famous people.

## Event sources
- [Wikipedia](https://www.wikipedia.org/) 🇮🇹🇺🇸🇬🇧🇫🇷🇩🇪🇪🇸🇵🇹 (other countries may work, not tested)
- [Accadde Oggi](https://www.accaddeoggi.it/) 🇮🇹

## Install
`pip install onthisday`

## Usage

### As a standalone script
In the root directory:

```
> python -m onthisday --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Commands:
  all     Print all the events of today
  last    Print last n events of today
  list    List the available sources (valid shorter names in brackets)
  random  Print random event of today
```

For the specific command options:

```
> python -m onthisday all --help

Usage: main.py all [OPTIONS]

  Print all the events of today

Options:
  --source TEXT  [default: wiki]
  --locale TEXT
  --help         Show this message and exit.
```

### As a library
_see the [example file](example.py) provided_ 

## Possible usages

### Shell greeting
Display a random event as the terminal emulator loads up.

For example, for the fish shell, one can add the following greeting function:
```angular2html
> function fish_greeting
      python -m onthisday random
  end

> funcsave fish_greeting
```

Close and reopen the terminal emulator and
```angular2html
[2005]  In Iraq inizia il processo all'ex-dittatore Saddam Hussein

~ via 🐍 v3.9.7 
➜ 
```

**known issue:** the script is not optimized and makes no use of caches.
The user experience with this kind of greeting message might not be the best as the command will take around 1 second to run.

## Issues
Please open issue on this GitHub repository for any error, suggestion or feature request.