# Hadoop MapReduce Emulation

This project is a Python-based implementation of the Hadoop MapReduce software framework for processing large datasets using a distributed and parallel approach.

## Components

The following components are included in this implementation:

- **main.py**: The entry point for the program that initiates the MapReduce job and coordinates the different components, including:
- **splitter.py**: Takes in the input data and splits it into smaller chunks that can be processed in parallel by the mapper servers.
- **mapper_servers.py**: Sets up multiple mapper servers that can process the data chunks in parallel. It distributes the data chunks across the servers and initiates the mapper function on each server. 
- **mapper.py**: The main processing unit that runs on each mapper server. It takes in a data chunk and applies a map function to it. The output of this component is a set of intermediate key-value pairs.
- **partitioner.py**: Takes the intermediate key-value pairs and partitions them into groups that can be processed by the reducer servers.
- **reducer_server.py**: Sets up multiple reducer servers that can process the data in parallel.
- **data_shuffler.py**: Distributes the intermediate key-value pairs across the reducer servers based on the partitioning. The output of this component is a set of key-value pairs.
- **data_grouper.py**: It sorts the data and initiates the reducer function on each server and groups them together into the final output.
- **job_tracker.py**: It creates the tasks and assigns it to TaskTracker.
- **task_tracker.py**: It calls the required functions and executes the task.


## Installation

To install and run this project, follow these steps:

1. Clone the repository:

`git clone https://github.com/__/DSCI-551-Project.git`

2. Run the program:

`python main.py input_file output_file reducer_count`

Where `input_file` is the path to the input file, and `output_file` is the desired output file name.

## Usage

To use this program, you will need to provide an input text file. The input file should contain the data to be processed.

After running the program, the output file will contain the results of the MapReduce job, which will be the word count.



