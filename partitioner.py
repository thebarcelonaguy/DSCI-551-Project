import glob
import hashlib
import os
import sys

# Partition the output of the mapper into files based on reducer count 
def partition(mapped_output_dir, num_reducers):
    partitioner_output = "partitioner_output"
    if not os.path.exists(partitioner_output):
        os.makedirs(partitioner_output)

    # Get a list of all the mapper files
    mapper_files = glob.glob(os.path.join(mapped_output_dir, "mapper*.txt"))
    
    # For each mapper file, create num_reducers output files
    for mapper_file in mapper_files:
        mapper_name = os.path.splitext(os.path.basename(mapper_file))[0]
        reducer_output_dir = os.path.join(partitioner_output, mapper_name)
        if not os.path.exists(reducer_output_dir):
            os.makedirs(reducer_output_dir)

        reducer_files = [open(os.path.join(reducer_output_dir, f"r{i}.out"), "w") for i in range(num_reducers)]

        # For each key-value pair in the mapper file, write it to the corresponding output file
        with open(mapper_file, 'r') as file:
            for line in file:
                tokens = line.strip().split()
                if len(tokens) == 2:
                    word, count = tokens
                    word_hash = int(hashlib.md5(word.encode()).hexdigest(), 16) % num_reducers
                    reducer_files[word_hash].write(f"{word},{count}\n")

        for f in reducer_files:
            f.close()

if __name__ == "__main__":
    mapped_output_dir = "mapper_output"
    num_reducers = int(sys.argv[1])
    partition(mapped_output_dir, num_reducers)
