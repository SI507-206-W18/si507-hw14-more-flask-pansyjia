import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []

def init(app):
    global entries
    try:

        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(clicked_id):
    #check every element in the list to see if that element is the element you are going to delete
    # have a for loop to check the id in the list to see if the element is the element you are going to delete
    global entries, GUESTBOOK_ENTRIES_FILE
    for ele in entries:
        if int(clicked_id) == list(ele.values())[-1]:
            try:
                entries.remove(ele)
            except:
                pass
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        empty_st = json.dumps(entries)
        f.write(empty_st)
        f.close()
    except:
        print("Please try again! Error" )

    print(entries)
