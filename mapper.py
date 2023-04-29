import socket
import string
import sys

# Define a class to handle mapping of a chunk
class Mapper:
    def __init__(self, chunk_filename, host, port):
        self.chunk_filename = chunk_filename
        self.host = host
        self.port = port

    # Process the chunk to create key-value pairs 
    def process_chunk(self):

        # Read in the chunk file and preprocess the text
        with open(self.chunk_filename, 'r') as file:
            data = file.read()
            data = data.translate(str.maketrans("", "", string.punctuation)).lower()
            words = data.split()

            # Create key-value pairs for each word in the chunk
            key_value_pairs = [(word, 1) for word in words]

            # Get the chunk number from the filename
            chunk_number = self.chunk_filename.split("_")[-1].split(".")[0]

            # Connect to the server and send the key-value pairs
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                print(f"Connected to server {self.host}:{self.port}")
                s.sendall(f"chunk_{chunk_number}\n".encode())
                for pair in key_value_pairs:
                    s.sendall(f"{pair[0]} {pair[1]}\n".encode())

# Defines a class which extends the Mapper class
class UserMapper(Mapper):
    def _init_(self, chunk_filename, host, port):
        super()._init_(chunk_filename, host, port)

    # Run the process_chunk() method
    def run(self):
        self.process_chunk()


if __name__ == "__main__":

    # Get the filename of the chunk to be processed and the port number of the server
    chunk_filename = sys.argv[1]
    host = "localhost"
    port = int(sys.argv[2])
    print(f"Starting mapper for {chunk_filename} on port {port}")
    user_mapper = UserMapper(chunk_filename, host, port)
    user_mapper.run()