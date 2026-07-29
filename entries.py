import sqlite3
import datetime
from variables import Variables

entries_path = Variables.config.entries_db_path
get_entries_query = "SELECT * FROM Entries WHERE Id = ?;"
save_entry_query = "INSERT INTO Entries(Title, Author, CreationDate, Content, Summary) VALUES (?,?,?,?,?);"

class Entry:
    def __init__(self, author:int, creationDate:datetime.datetime, content:str, summary:str=None, title:str=None):
        self.title = title
        self.author = author
        self.creationDate = creationDate
        self.content = content
        self.summary = summary
        if self.summary == None:
            self.summary = "This entry was not summarised."
        if self.title == None:
            now = self.creationDate.replace(microsecond=0).timestamp()
            date_time = datetime.datetime.fromtimestamp(now)
            self.title = (f"Untitled entry {date_time}")
    def __str__(self):
        return(f"Entry {self.title}, created by {self.author} at {self.creationDate} with summary {self.summary}\nContent:\n{self.content}")

def get_entries(id):
    with sqlite3.connect(entries_path) as conn:
        cur = conn.cursor()
        cur.execute(get_entries_query, (id,))
        return cur.fetchall()

def save_entry(Entry):
    with sqlite3.connect(entries_path) as conn:
        cur = conn.cursor()
        cur.execute(save_entry_query, (Entry.title, Entry.author, Entry.creationDate, Entry.content, Entry.summary))

if __name__ == "__main__":
    entry = Entry(
        author=1,
        creationDate=datetime.datetime.now(),
        content="""
This is example content since I cant think hard enough on how to properly implement this.
Welcome to my world chuds
I can\'t code, fun...
Multiline strings are amazing however. :)
"""
    )
    print(entry)
    save_entry(entry)