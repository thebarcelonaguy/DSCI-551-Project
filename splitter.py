def split_file_by_size(input_file, block_size):
    """
    Split a text file into chunks of a specified size (in bytes),
    ensuring that each chunk ends on a complete word.
    """
    with open(input_file, 'r') as f:
        # Read the entire file into memory
        data = f.read()

    # Split the file into blocks of the specified size
    blocks = []
    start = 0
    while start < len(data):
        block = data[start:start + block_size]

        # Check if the block ends in the middle of a word
        if start + len(block) < len(data):
            next_word_start = data.find(' ', start + len(block))
            if next_word_start != -1:
                # The block ends in the middle of a word, remove the incomplete word from the block
                block = block[:next_word_start - start]

        blocks.append(block)
        start += len(block)

    # Add the remaining part of a word to the next block
    for i in range(len(blocks) - 1):
        last_word_end = blocks[i].rfind(' ')
        if last_word_end != -1 and len(blocks[i]) - last_word_end <= block_size:
            remaining_word = blocks[i][last_word_end:]
            blocks[i] = blocks[i][:last_word_end]
            blocks[i+1] = remaining_word + blocks[i+1]

    # Check if the last block is too small
    if len(blocks) > 0 and len(blocks[-1]) < block_size:
        if len(data) - len(blocks[-1]) <= block_size:
            # The last block is too small, and the remaining data is small enough to fit in the last block
            blocks[-1] += data[len(blocks[-1]):]
        else:
            # The last block is too small, but there's too much remaining data to fit in the last block
            # so we make an exception and let the last block exceed the block size
            blocks[-1] += data[len(blocks[-1]):len(blocks[-1]) + block_size]

    # Write each block to a separate file in the output directory
    for i, block in enumerate(blocks):
        filename = f'block_{i}.txt'
        with open(filename, 'w') as f:
            f.write(block)


input_file = 'input.txt'
#output_directory = 'DSCI-551-PROJECT-MAIN'
block_size = 500000  # 1 MB
split_file_by_size(input_file, block_size)
