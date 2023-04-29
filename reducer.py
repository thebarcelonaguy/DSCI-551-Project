import os

class Reducer:
    def __init__(self, input_file):
        """
        Initializes a new Reducer object with the given input file path.

        :param input_file: the path to the input file
        """
        self.input_file = input_file
        
    def get_input_file(self):
        """
        Returns the path to the input file.

        :return: the path to the input file
        """
        return self.input_file


class UserReducer(Reducer):
    def __init__(self, input_file):
        """
        Initializes a new UserReducer object with the given input file path.
        This class extends the Reducer class.

        :param input_file: the path to the input file
        """
        super().__init__(input_file)
        
    def word_count(self):
        """
        Counts the occurrences of each word in the input file, and writes the result to an output file.

        The output file is located in a directory called 'reducer_output', which is created if it does not exist.
        The output file has the same name as the input file, but with the 'reducer_output' directory path and '.txt'
        extension appended to it.

        Each line in the output file has the format 'word,count', where 'word' is a word in the input file and
        'count' is the number of occurrences of that word.

        :return: None
        """
        word_counts = {}
        with open(self.input_file, 'r') as file:
            for line in file:
                word, count = line.strip().split(',')
                if word in word_counts:
                    word_counts[word] += int(count)
                else:
                    word_counts[word] = int(count)

        reducer_output_dir = "reducer_output"
        if not os.path.exists(reducer_output_dir):
            os.makedirs(reducer_output_dir)

        output_file = os.path.join(reducer_output_dir, os.path.basename(self.input_file))
        with open(output_file, 'w') as file:
            for word, count in word_counts.items():
                file.write(f"{word},{count}\n")


