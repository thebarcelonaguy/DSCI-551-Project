import hashlib
import math
import re


class ConsistentHash:
    def __init__(self, nodes, replicas=100):
        self.replicas = replicas
        self.ring = {}
        for node in nodes:
            for i in range(replicas):
                key = self.hash(f'{node}:{i}')
                self.ring[key] = node
        self.keys = sorted(self.ring.keys())

    def get_node(self, key):
        if not self.ring:
            return None
        hashval = self.hash(key)
        for i in range(len(self.keys)):
            if hashval <= self.keys[i]:
                return self.ring[self.keys[i]]
        return self.ring[self.keys[0]]

    def hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

def mapper(input_file, num_output_files):
    """A mapper function that reads a text file and partitions the data to different output files"""

    # Define a consistent hash-based partitioner function
    nodes = [f'reducer{i}' for i in range(num_output_files)]
    partitioner = ConsistentHash(nodes)

    # Open the input file
    with open(input_file, 'r') as f:

        # Loop through each line in the file
        for line in f:

            # Remove any leading/trailing whitespace characters from the line
            line = line.strip()

            # If the line is not blank, emit the line as a key-value pair
            if line:
                key = line
                value = 1

                # Assign the key to a reducer using the partitioner function
                partition = partitioner.get_node(key)

                # Write the key-value pair to the corresponding output file
                with open(f'{partition}.txt', 'a') as outfile:
                    outfile.write(f'{key}\t{value}\n')

mapper("input.txt",10)