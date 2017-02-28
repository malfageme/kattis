import sys

notes = "GFEDCBAgfedcba"

num_notes = int(sys.stdin.readline())
notes_list = sys.stdin.readline().split()

for i in range(len(notes)):
    note = notes[i]
    text = "{}: ".format(note)
    no_char = "-" if i%2==1 and i!=11 else " "
    last_note = None
    for new_note in notes_list:
        rep = 1
        note_str = new_note[0]
        #if last_note == note_str:
        if last_note:
            text += no_char
        last_note = note_str
        if len(new_note) > 1:
            rep = int(new_note[1:])
        text += ('*' if note_str==note else no_char) * rep

    print text


