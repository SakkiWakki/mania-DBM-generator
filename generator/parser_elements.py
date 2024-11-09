from pyparsing import *

# Basic values
comment = "//" + restOfLine
string = Regex(r'[^,:\n]+').setParseAction(lambda t: str(t[0]))
integer = Regex(r"-?\d+").setParseAction(lambda t: int(t[0]))
decimal = Regex(r"-?\d+\.\d+").setParseAction(lambda t: float(t[0]))

# Key value pairs
key = Word(alphanums) + Suppress(":")
value = decimal | integer | string
key_value_pair = Group(key + Optional(Suppress(Literal(" "))) + Optional(value).leaveWhitespace() + Suppress(line_end))

# Headers
section_header = Suppress("[") + Word(alphas) + Suppress("]")

# Lists
delim_list = delimitedList((decimal | integer | string), allow_trailing_delim=True, delim=oneOf(", :"), combine=True, min=3)

# Sections
version_line = Group(Literal("osu file format v") + Word(nums))
keyvalue_section = Group(section_header + OneOrMore(Dict(key_value_pair)))
list_section = Group(section_header + OneOrMore(delim_list))

# Grammar of the entire file
osu_parser = Dict(version_line) + ZeroOrMore(
        Dict(keyvalue_section) | Dict(list_section)
    )
osu_parser.ignore(comment)

