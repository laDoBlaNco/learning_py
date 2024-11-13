# Varible Names

# Since python variables don't have any type spelled out in the source
# code, it's extra helpful to give meaningful names to your variables to
# remind yourself fo what's going on. So use 'name' if its a single name,
# and 'names' if its a list of names, and 'tuples' if its a list of tuples.
# Many basic py errors result from forgetting what type of values is in each
# variable, so use your variable names (which is all you have really) to
# help keep things straight.

# As far as atcual naming goes, some languages prefer underscored_parts which
# is called snake_case, but other languages prefer camelCasing. In general,
# py prefers the underscore method but guides developers to defer to camelCasing
# if integrating into existing py code that already uses that style. Readability
# counts. 

# As expected, keywords like 'if' and 'while' cannot be used as variable names
# you'll get a syntax error if you do. However, be careful not to use built-ins
# as variable names. For example, while 'str', 'list' and 'print' might seem
# like good names, you'd be overriding those system variables. Built-ins are
# not keywords and thus, are susceptible to inadvertent use by new py devs.