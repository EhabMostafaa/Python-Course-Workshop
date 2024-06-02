PEOPLE = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)
]

def format_sort_record(tuple_people):
    updated_records = []
    for row in tuple_people:
        updated_records.append((row[1], row[0], row[2]))
    
    template = '{0:10} {1:10} {2:5.2f}'
    formatted_records = [template.format(*record) for record in updated_records]
    
    return '\n'.join(formatted_records)

print(format_sort_record(PEOPLE))
