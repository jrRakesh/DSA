# ============================================================
# HUFFMAN COMPRESSION
# ============================================================
# This program can:
# 1. Read a text file
# 2. Count the frequency of each character
# 3. Build a Huffman Tree
# 4. Generate Huffman codes
# 5. Compress the text
# 6. Decompress the compressed file
#
# This version does NOT use:
# - Classes / OOP
# - heapq
# - Counter
# - Any external library
# ============================================================


# ============================================================
# 1. COUNT FREQUENCY
# ============================================================

def count_frequency(text):
    # Create an empty dictionary.
    # It will store:
    #
    # character -> frequency
    #
    # Example:
    # {'a': 3, 'b': 2, 'c': 1}
    frequency = {}

    # Go through every character in the text.
    for char in text:

        # Check if the character is already in the dictionary.
        if char in frequency:

            # If it already exists, increase its frequency by 1.
            frequency[char] += 1

        else:

            # If it does not exist, add it with frequency 1.
            frequency[char] = 1

    # Return the completed frequency dictionary.
    return frequency


# ============================================================
# 2. FIND THE SMALLEST NODE
# ============================================================

def find_min(nodes):

    # We assume that the first node is the smallest.
    min_index = 0

    # Start checking from the second node.
    # range(1, len(nodes)) means:
    # 1, 2, 3, 4, ...
    for i in range(1, len(nodes)):

        # nodes[i][1] is the frequency of the current node.
        #
        # nodes[min_index][1] is the frequency of the
        # node we currently think is the smallest.
        if nodes[i][1] < nodes[min_index][1]:

            # If current node has smaller frequency,
            # remember its index.
            min_index = i

    # Return the index of the smallest node.
    return min_index


# ============================================================
# 3. BUILD HUFFMAN TREE
# ============================================================

def build_tree(frequency):

    # Create an empty list.
    #
    # Each node will look like:
    #
    # [character, frequency, left, right]
    #
    # Example:
    #
    # ['a', 5, None, None]
    #
    # means:
    # character = 'a'
    # frequency = 5
    # left = None
    # right = None
    nodes = []

    # Go through every character in the frequency dictionary.
    for char in frequency:

        # Create a node for every character.
        #
        # frequency[char] gives the frequency of that character.
        nodes.append([
            char,               # character
            frequency[char],    # frequency
            None,               # left child
            None                # right child
        ])

    # We continue until only one node remains.
    #
    # That final node will be the root of our Huffman Tree.
    while len(nodes) > 1:

        # Find the index of the node with the smallest frequency.
        first_index = find_min(nodes)

        # Remove that node from the list.
        #
        # pop() removes the item and also returns it.
        left = nodes.pop(first_index)

        # Find the second smallest node.
        second_index = find_min(nodes)

        # Remove the second smallest node.
        right = nodes.pop(second_index)

        # Create a new internal node.
        #
        # It does not represent a character,
        # so character = None.
        #
        # Its frequency is the sum of the two nodes.
        new_node = [
            None,                       # No character
            left[1] + right[1],         # Total frequency
            left,                       # Left child
            right                       # Right child
        ]

        # Add the new node back into the list.
        nodes.append(new_node)

    # There should now be only one node.
    #
    # This is the root of the Huffman Tree.
    return nodes[0]


# ============================================================
# 4. GENERATE HUFFMAN CODES
# ============================================================

def generate_codes(node, code, codes):

    # Check whether the current node is empty.
    if node is None:

        # If there is no node, stop.
        return

    # node[0] contains the character.
    #
    # If it is not None, this is a leaf node.
    if node[0] is not None:

        # Store the Huffman code.
        #
        # Example:
        # codes['a'] = '010'
        codes[node[0]] = code

        # We have reached the end of this branch.
        return

    # --------------------------------------------------------
    # Go to the LEFT child.
    # We add 0 to the code.
    # --------------------------------------------------------

    generate_codes(
        node[2],          # left child
        code + "0",       # add 0
        codes             # dictionary containing codes
    )

    # --------------------------------------------------------
    # Go to the RIGHT child.
    # We add 1 to the code.
    # --------------------------------------------------------

    generate_codes(
        node[3],          # right child
        code + "1",       # add 1
        codes             # dictionary containing codes
    )


# ============================================================
# 5. COMPRESS THE FILE
# ============================================================

def compress(input_file, output_file):

    # Open the input text file in read mode.
    file = open(input_file, "r")

    # Read the entire file into the variable 'text'.
    text = file.read()

    # Close the file.
    file.close()

    # Check if the file is empty.
    if text == "":

        # Tell the user that the file is empty.
        print("File is empty.")

        # Stop the function.
        return

    # --------------------------------------------------------
    # Count character frequencies
    # --------------------------------------------------------

    frequency = count_frequency(text)

    # Print a heading.
    print("\nCharacter Frequency:")

    # Go through every character in the frequency dictionary.
    for char in frequency:

        # Print the character and its frequency.
        #
        # repr(char) is used because it makes spaces and
        # special characters easier to see.
        #
        # For example:
        # repr(' ') gives ' '
        print(repr(char), ":", frequency[char])

    # --------------------------------------------------------
    # Build the Huffman Tree
    # --------------------------------------------------------

    root = build_tree(frequency)

    # --------------------------------------------------------
    # Generate Huffman Codes
    # --------------------------------------------------------

    # Create an empty dictionary for the codes.
    codes = {}

    # Start from the root of the tree.
    #
    # The initial code is an empty string.
    generate_codes(root, "", codes)

    # --------------------------------------------------------
    # Special case:
    # If the file contains only one unique character,
    # its code would normally become "".
    #
    # We change it to "0".
    # --------------------------------------------------------

    if len(codes) == 1:

        # Get the only character.
        only_char = list(codes.keys())[0]

        # Give it the code 0.
        codes[only_char] = "0"

    # Print Huffman codes.
    print("\nHuffman Codes:")

    # Go through every character.
    for char in codes:

        # Print character and its Huffman code.
        print(repr(char), ":", codes[char])

    # --------------------------------------------------------
    # Convert original text into Huffman binary codes.
    # --------------------------------------------------------

    # Start with an empty string.
    binary = ""

    # Go through every character in the original text.
    for char in text:

        # Get the Huffman code of that character
        # and add it to binary.
        #
        # Example:
        #
        # text = "abc"
        #
        # a = 0
        # b = 10
        # c = 11
        #
        # binary becomes:
        # 01011
        binary += codes[char]

    # --------------------------------------------------------
    # Save compressed information
    # --------------------------------------------------------

    # Open the output file in write mode.
    file = open(output_file, "w")

    # First save the Huffman codes.
    #
    # ord(char) converts a character to a number.
    #
    # Example:
    # ord('A') = 65
    # ord('a') = 97
    #
    # This makes storing spaces and special characters easier.
    for char in codes:

        # Write:
        #
        # ASCII_VALUE:Huffman_Code
        #
        # Example:
        # 97:0
        # 98:10
        file.write(
            str(ord(char)) + ":" + codes[char] + "\n"
        )

    # Write a special word to tell us that
    # the Huffman code section has ended.
    file.write("DATA\n")

    # Write the actual compressed binary data.
    file.write(binary)

    # Close the output file.
    file.close()

    # --------------------------------------------------------
    # Display compression information
    # --------------------------------------------------------

    print("\nCompression successful!")

    # Normally a character takes 8 bits in a text file.
    print("Original bits :", len(text) * 8)

    # Our Huffman representation uses the number of bits
    # contained in 'binary'.
    print("Compressed bits:", len(binary))


# ============================================================
# 6. DECOMPRESS THE FILE
# ============================================================

def decompress(input_file, output_file):

    # Open the compressed file.
    file = open(input_file, "r")

    # Create an empty dictionary.
    #
    # This time we will store:
    #
    # Huffman code -> character
    #
    # Example:
    # {'0': 'a', '10': 'b', '11': 'c'}
    codes = {}

    # Start with an empty binary string.
    binary = ""

    # This variable tells us whether we have reached
    # the DATA section of the file.
    data_started = False

    # Read the file one line at a time.
    for line in file:

        # Remove the newline character from the end.
        line = line.strip()

        # Check if we have reached "DATA".
        if line == "DATA":

            # From the next line onward,
            # everything is compressed data.
            data_started = True

            # Move to the next line.
            continue

        # ----------------------------------------------------
        # If DATA section has started
        # ----------------------------------------------------

        if data_started:

            # Add the binary data to 'binary'.
            binary += line

        # ----------------------------------------------------
        # Otherwise we are still reading Huffman codes.
        # ----------------------------------------------------

        else:

            # Split something like:
            #
            # 97:0
            #
            # into:
            #
            # ['97', '0']
            parts = line.split(":")

            # First part is the ASCII number.
            ascii_value = int(parts[0])

            # Second part is the Huffman code.
            code = parts[1]

            # Convert ASCII number back to a character.
            #
            # Example:
            # chr(97) = 'a'
            char = chr(ascii_value)

            # Store the code and character.
            #
            # Example:
            # codes['0'] = 'a'
            codes[code] = char

    # Close the compressed file.
    file.close()

    # --------------------------------------------------------
    # Decode the binary data
    # --------------------------------------------------------

    # Temporary string for storing bits.
    current = ""

    # This will contain the final original text.
    text = ""

    # Go through every bit.
    for bit in binary:

        # Add the current bit.
        #
        # Example:
        #
        # current = ""
        # bit = "0"
        #
        # current becomes "0"
        current += bit

        # Check whether the current sequence
        # is a valid Huffman code.
        if current in codes:

            # If it is a valid code,
            # convert it back to its character.
            text += codes[current]

            # Start looking for the next character.
            current = ""

    # --------------------------------------------------------
    # Save decompressed text
    # --------------------------------------------------------

    # Open the output file.
    file = open(output_file, "w")

    # Write the original text.
    file.write(text)

    # Close the file.
    file.close()

    # Tell the user that decompression is complete.
    print("Decompression successful!")


# ============================================================
# 7. MAIN PROGRAM
# ============================================================

# Display program title.
print("HUFFMAN COMPRESSION")

# Ask the user what they want to do.
choice = input(
    "1. Compress\n"
    "2. Decompress\n"
    "Enter choice: "
)

# ============================================================
# If user chooses compression
# ============================================================

if choice == "1":

    # Ask for the input text file.
    input_file = input("Enter input file: ")

    # Ask for the output compressed file.
    output_file = input("Enter output file: ")

    # Call the compress function.
    compress(input_file, output_file)


# ============================================================
# If user chooses decompression
# ============================================================

elif choice == "2":

    # Ask for the compressed file.
    input_file = input("Enter compressed file: ")

    # Ask where to save the decompressed text.
    output_file = input("Enter output file: ")

    # Call the decompress function.
    decompress(input_file, output_file)


# ============================================================
# If user enters anything other than 1 or 2
# ============================================================

else:

    # Display an error message.
    print("Invalid choice!")
    