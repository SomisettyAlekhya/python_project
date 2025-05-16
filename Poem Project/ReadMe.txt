
Poem XML Query Server-Client Project

This project implements a multithreaded Client-Server application in Python that analyzes a poem from a `.txt` file, processes it, and returns lines containing a specified word in XML format. It demonstrates:

- Socket programming
- Threading
- File parsing and cleaning
- XML generation
- Modular programming

Project Structure:
------------------
client.py             # Client script that sends a word to the server and displays the XML response
server.py             # Multithreaded server that processes poem queries
poem.py               # Poem processing utility with various cleaning methods
parser.py             # Builds an XML structure from matching lines
poem.txt              # The original input poem text
poem_result.xml       # Sample XML output for the word 'man'

How It Works:
-------------
1. Start the Server:
   Run the `server.py`:
   > python server.py
   This starts a socket server at 127.0.0.1:5656, waits for client connections, and processes queries.

2. Run the Client:
   In another terminal:
   > python client.py
   Then input a word (e.g., `man`) to search.

Components:
-----------
- poem.py: Loads and cleans the poem, provides `getLines(word)`
- parser.py: Builds XML output using `build_xml(word, lines)`
- server.py: Listens for client connections and processes them using threads
- client.py: Sends a word to server and prints the XML response

Example Output:
---------------
Input word: man
Response:
<lines word="man" total="1">
    <line line_number="0">Breathes there the man</line>
</lines>

Features:
---------
- Modular Design
- Threaded Client Handling
- Dynamic XML Generation
- Clean and Maintainable Code

Requirements:
-------------
- Python 3.x
- No external libraries required

Future Improvements:
---------------------
- Case-insensitive search
- GUI client
- Support multiple poem files
- Save search history

