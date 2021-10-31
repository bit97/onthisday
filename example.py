from onthisday import Today

SUPPORTED_LOCALES = [
    "it",
    "en",
    "es",
    "pt",
    "de",
    "fr"
]

# Wikipedia source
wiki = Today("wiki", SUPPORTED_LOCALES[0])
# or
# wiki = Today()
# as the wikipedia event is the default one

# Retrieve all the events
print(wiki.all())

# Retrieve the last n events
print(wiki.last(5))

# Retrieve the last event
print(wiki.last()[0])

# Retrieve a random event
print(wiki.random())

# Same, but with year range
try:
    print(wiki.random(from_year=1980, to_year=2005))
except IndexError:
    print("No event for specified range")

# Same, but with BC years
try:
    print(wiki.random(to_year=-5))  # i.e. until 5 BC
except IndexError:
    print("No event for specified range")