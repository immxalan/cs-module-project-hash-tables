class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
# algorithm fnv-1 is
#     hash := FNV_offset_basis do  14695981039346656037

#     for each byte_of_data to be hashed
#         hash := hash × FNV_prime (1099511628211)
#         hash := hash XOR byte_of_data

#     return hash 

# def djb2(key):
#   hash = 5381
#   for c in key:
#     hash = (hash * 33) + ord(c)
#   return hash

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.min_capacity = MIN_CAPACITY
        if capacity > self.min_capacity:
            self.capacity = capacity
        else:
            self.capacity = self.min_capacity
        self.storage = [None] * self.capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        hash = 14695981039346656037
        for x in key:
            hash = hash ^ ord(x)
            hash = (hash * 1099411628211)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hashed = 5381
        for c in key:
            hashed = (hashed * 33) + ord(c)
            return hashed


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # index = self.hash_index(key)
        # if self.array[index] is not None:
        #     for kvp in self.array[index]:
        #         if kvp[0] == key:
        #             kvp[1] = value
        #             break

        # i = self.hash_index(key)
        # self.storage[i] = value
        currIndex = self.hash_index(key)
        if(self.storage[currIndex] == None):
            self.storage[currIndex] = HashTableEntry(key, value)
            self.count += 1
        else:
            curr = self.storage[currIndex]
            while curr.next != None and curr.key != key:
                curr = curr.next
            if curr.key == key:
                curr.value = value
            else:
                new_entry = HashTableEntry(key, value)
                new_entry.next = self.storage[currIndex]
                self.storage[currIndex] = new_entry
                self.count += 1
        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # i = self.hash_index(key)
        # if self.storage[i] == None:
        #     print('There is nothing at this index')
        # else:
        #     self.storage[i] = None
        currIndex = self.hash_index(key)
        if self.storage[currIndex].key == key:
            if self.storage[currIndex].next == None:
                self.storage[currIndex] = None
                self.count -= 1
            else:
                new_head = self.storage[currIndex].next
                self.storage[currIndex].next = None
                self.storage[currIndex] = new_head
                self.count -= 1
        else:
            if self.storage[currIndex] == None:
                return None
            else:
                curr = self.storage[currIndex]
                prev = None
                while curr.next is not None and curr.key != key:
                    prev = curr
                    curr = curr.next
                if curr.key == key:
                    prev.next = curr.next
                    self.count -= 1
                    return curr.value
                else:
                    return None
        if self.get_load_factor() < .2:
            if self.capacity/2 > 8:
                self.resize(self.capacity//2)
            elif self.capacity > 8:
                self.resize(8)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # i = self.hash_index(key)
        # node = self.storage[i]
        # if node is not None:
        #     return node
        # else:
        #     print("No node found")
        #     return None
        index = self.hash_index(key)
        if self.storage[index] is not None and self.storage[index].key == key:
            return self.storage[index].value
        elif self.storage[index] is None:
            return None
        else:
            curr = self.storage[index]
            while curr.next != None and curr.key != key:
                curr = self.storage[index].next
            if curr == None:
                return None
            else:
                return curr.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_table = self.storage[:]
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        for i in range(len(old_table)):
            if old_table[i] is not None:
                curr = old_table[i]
                self.put(curr.key, curr.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
