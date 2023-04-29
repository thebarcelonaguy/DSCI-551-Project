import os
import socket
import sys
import threading

# This function handles the client connection and saves the mapper output to a file.
def handle_client(conn):
    received_data = b''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        received_data += data

    # Extract the chunk number from the first line of received data
    lines = received_data.decode().split("\n")[:-1]
    chunk_number = lines.pop(0).split("_")[-1]

    # Create a directory for the output files if it does not exist
    output_dir = "mapper_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

     # Save the intermediate key-value pairs to a file
    with open(f"{output_dir}/mapper{chunk_number}.txt", "w") as f:
        for pair in lines:
            f.write(pair + "\n")

     # Close the connection and print a message indicating successful completion          
    print(f"Output saved for chunk {chunk_number}")
    conn.close()

# This function starts the mapper server on the specified port.
def start_mapper_server(port):
    host = "localhost"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Mapper server listening on port {port}")

        # Wait for a client to connect and spawn a new thread to handle the connection
        while True:
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            thread = threading.Thread(target=handle_client, args=(conn,))
            thread.start()

if __name__ == "__main__":
    
    # Get the list of input files and start a mapper server for each file on a separate port
    input_dir = "splitter_output"
    files = os.listdir(input_dir)
    num_servers = len(files)
    for i, file in enumerate(files):      
        port = 8000 + i
        print(f"Starting mapper server for {file} on port {port}")
        thread = threading.Thread(target=start_mapper_server, args=(port,))
        thread.start()

    print(f"{num_servers} mapper servers started.")
