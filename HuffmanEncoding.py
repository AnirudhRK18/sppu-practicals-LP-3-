import heapq

def huffman_encoding(text):
    # Calculate frequency of each character
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Create a priority queue from the frequency dictionary
    heap = [[weight, [char]] for char, weight in freq.items()]  # Store as [weight, [char]]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pop the two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Create a new internal node with these two nodes as children
        merged = [left[0] + right[0], left[1] + right[1]]  # Combine weights and characters
        heapq.heappush(heap, merged)

    # This is the root node of the Huffman Tree
    huffman_tree = heap[0]

    huffman_code = {}

    # Recursive function to generate codes
    def encode(node, code):
        if len(node[1]) == 1:  # If it's a leaf node
            huffman_code[node[1][0]] = code
        else:
            # Traverse left and right children
            # The left child will always be the first element in node[1]
            encode([node[0], node[1][:len(node[1]) // 2]], code + '0')  # Left half
            encode([node[0], node[1][len(node[1]) // 2:]], code + '1')  # Right half

    # Start encoding from the root of the tree
    encode(huffman_tree, '')

    # Encode the original text using the generated codes
    encoded_text = ''.join(huffman_code[char] for char in text)
    return encoded_text, huffman_code

if __name__ == "__main__":
    text = "text" # instead of 'encoding example' try different input
    encoded_text, huffman_code = huffman_encoding(text)

    print("Encoded text:", encoded_text)
    print("Huffman code:", huffman_code)
