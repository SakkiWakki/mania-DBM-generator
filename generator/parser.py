from parser_elements import osu_parser

def parse_osu_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # Parse the content with osu_parser
    parsed_data = osu_parser.parseString(file_content)
    
    return parsed_data
from pprint import pprint
o = parse_osu_file(r'E:\Rhythm Games\Rhythm Game Files\Osu Songs\1075603 HyuN - The Apocalypse\HyuN - The Apocalypse (Capu) [Apocalyptic Oni].osu')

pprint(o.asDict())
# print(o["TimingPoints"])

