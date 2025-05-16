import socket

host = "127.0.0.1"
port = 5656

s1 = socket.socket()

try:
    s1.connect((host, port))
    word = input("Enter a word to search in the poem: ")
    s1.send(word.encode("utf-8"))

    # Receive XML data from server
    data = s1.recv(10000)

    # Save the XML response to a file
    with open("poem_result.xml", "wb") as f:
        f.write(data)

    decoded_data = data.decode("utf-8").strip()

    # Check for error response
    if decoded_data.startswith("<error>"):
        print("Server Error:", decoded_data)
    else:
        print("\nReceived XML Response:\n")

        lines = decoded_data.splitlines()

        for line in lines:
            print(line.strip())

except Exception as e:
    print("Connection Error:", e)

finally:
    s1.close()