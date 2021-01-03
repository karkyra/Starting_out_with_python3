# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] }
# and returns a dictionary of objects like { "name": "John", "top_note": 5 }.


def top_note(student):

    a = sorted(student.get('notes'))[-1]
    new_student = {key:val for key, val in student.items() if key != 'notes'}
    new_student['top_note'] = a
    return new_student


print(top_note({ "name": "John", "notes": [3, 5, 4] }))
print(top_note({ "name": "Max", "notes": [1, 4, 6] }))
