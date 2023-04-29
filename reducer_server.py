import socket
import threading
import sys
from reducer import Reducer
from reducer import UserReducer

lock = threading.Lock()

# Define a function to handle each client that connects to the server
def handle_client(client_socket, sorted_file):

    # Use the lock to prevent multiple threads from printing at the same time
    with lock:
        print(f"[*] Received file {sorted_file}")
        #Call Extended Reducer
        reducer = UserReducer(sorted_file)
        reducer.word_count()
    client_socket.close()

# Define a function to start the reducer server on a specified port
def start_reducer_server(port):

    # Create a socket object and bind it to the specified port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))

    # Start listening for incoming client connections
    server.listen(5)
    print(f"[*] Listening on port {port}")

    # Continuously accept incoming client connections and handle them with a new thread
    while True:
        client, _ = server.accept()
        sorted_file = client.recv(1024).decode('utf-8')

        # Send 'OK' response immediately after receiving the file
        client.sendall('OK'.encode('utf-8'))

        # Create a new thread to handle the client connection
        client_handler = threading.Thread(target=handle_client, args=(client, sorted_file))
        client_handler.start()

if __name__ == "__main__":

    # Get the number of reducers from the command line arguments
    num_reducers = int(sys.argv[1])

    # Calculate the ports for the reducer servers
    reducer_ports = [5040 + i for i in range(num_reducers)]

    # Start a new thread for each reducer server
    server_threads = []

    for port in reducer_ports:
        server_thread = threading.Thread(target=start_reducer_server, args=(port,))
        server_threads.append(server_thread)
        server_thread.start()

    # Wait for all threads to finish before exiting
    for server_thread in server_threads:
        server_thread.join()
