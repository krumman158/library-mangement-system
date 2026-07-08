from library.config import DELIMITER
def parse_line(line:str)->dict:
    parts=line.strip().split(DELIMITER)
    return{
        'id':int(parts[0]),
        'title':parts[1],
        'author':parts[2],
        'year':parts[3],
        'available':parts[4]=='True'
    }

def to_line(book:dict)->str:
    return DELIMITER.join([
        str(book['id']),
        str(book['title']),
        str(book['author']),
        str(book['year']),
        str(book['available']),
    ])