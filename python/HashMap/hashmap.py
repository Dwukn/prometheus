class HashMap:
    def __init__(self, size=100):
        """
        Initialize the HashMap with a given size (default is 100).
        The size determines how many buckets (slots) the hash map will have.
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Create an array of empty lists (buckets)
        self.count = 0  # Keep track of the number of elements in the map

    def _hash(self, key):
        """
        Private helper function that hashes a key to an index.
        It uses Python's built-in `hash()` function and the modulo operator
        to ensure the hash value fits within the table size.
        """
        return hash(key) % self.size

    def _resize(self):
        """
        Resize the hash map when the load factor is too high.
        It doubles the size of the table and rehashes all the existing keys.
        """
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]

        # Rehash and insert all existing key-value pairs into the new table
        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % new_size
                new_table[new_index].append((key, value))

        # Update the size and the table reference
        self.size = new_size
        self.table = new_table

    def insert(self, key, value):
        """
        Insert a key-value pair into the HashMap.
        If the key already exists, it updates the value.
        """
        # Check if we need to resize the hash map due to load factor
        if self.count / self.size > 0.7:  # Resize if load factor > 70%
            self._resize()

        index = self._hash(key)  # Find the index for the key
        bucket = self.table[index]  # Access the bucket at that index

        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update the value for existing key
                return

        # If key doesn't exist, append the new key-value pair to the bucket
        bucket.append((key, value))
        self.count += 1  # Increase the element count

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        Returns None if the key doesn't exist.
        """
        index = self._hash(key)  # Find the index for the key
        bucket = self.table[index]  # Access the bucket at that index

        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v  # Return the value if found

        return None  # Return None if the key isn't found

    def remove(self, key):
        """
        Remove the key-value pair from the HashMap.
        If the key doesn't exist, it does nothing.
        """
        index = self._hash(key)  # Find the index for the key
        bucket = self.table[index]  # Access the bucket at that index

        # Search for the key and remove the key-value pair if found
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)  # Remove the key-value pair from the bucket
                self.count -= 1  # Decrease the element count
                return

    def contains(self, key):
        """
        Check if a key exists in the HashMap.
        Returns True if the key exists, otherwise False.
        """
        index = self._hash(key)  # Find the index for the key
        bucket = self.table[index]  # Access the bucket at that index

        # Check if the key is in the bucket
        for k, v in bucket:
            if k == key:
                return True  # Key found

        return False  # Key not found

    def print_map(self):
        """
        Print the entire hash map.
        It prints each bucket and its contents in a human-readable format.
        """
        print("HashMap contents:")
        for index, bucket in enumerate(self.table):
            if bucket:  # Only print non-empty buckets
                print(f"Index {index}: {bucket}")

# Example usage:
hash_map = HashMap()

# Insert some key-value pairs
hash_map.insert("name", "Alice")
hash_map.insert("age", 25)
hash_map.insert("city", "New York")
hash_map.insert("job", "Engineer")

# Print the current state of the HashMap
hash_map.print_map()

# Get values associated with keys
print(hash_map.get("name"))  # Output: Alice
print(hash_map.get("age"))   # Output: 25
print(hash_map.get("country"))  # Output: None

# Check if a key exists
print(hash_map.contains("city"))  # Output: True
print(hash_map.contains("country"))  # Output: False

# Remove a key-value pair
hash_map.remove("age")

# Print the updated state of the HashMap after removal
hash_map.print_map()

# Try getting the removed value
print(hash_map.get("age"))  # Output: None
