def main():
    # Store a list of words
    word_list = ["apple", "banana", "orange", "kiwi", "pineapple", "grape"]

    # Create a new list containing only words with an odd number of characters
    odd_length_words = [word for word in word_list if len(word) % 2 != 0]

    # Print the new list
    print("Words with an odd number of characters:", odd_length_words)

if __name__ == "__main__":
    main()

    
