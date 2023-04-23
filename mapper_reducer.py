import hashlib
import math
import re


class Mapper:
    def mapper(self,input_file):
        value=0
        """A mapper function that reads a text file and partitions the data to different output files"""

        # Define a consistent hash-based partitioner function
        nodes = 5
        text = ""
        # Open the input file
        with open(input_file, 'r') as f:

            # Loop through each line in the file
            for line in f:

                # Remove any leading/trailing whitespace characters from the line
                line = line.strip()

                # If the line is not blank, emit the line as a key-value pair
                if line:
                    key = line
                    value = value+1
                    text+=str(value)+","+str(key)+"\n"
                    # Write the key-value pair to the corresponding output file
            with open(f'output.txt', 'w') as outfile:
                outfile.write(text)





obj1=Mapper()
obj1.mapper("riten_input.txt")


