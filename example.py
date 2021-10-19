from onthisday import Today


# Wikipedia source
wiki = Today('wiki')
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
print(wiki.random(from_year=1980, to_year=2005))

# Same, but with BC years
print(wiki.random(to_year=-5))  # i.e. until 5 BC
