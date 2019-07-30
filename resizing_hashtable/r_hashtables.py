

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None for i in range(capacity)]
        self.capacity = capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for item in string:
        hash = ((hash << 5) + hash) + ord(item)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashkey = hash(key, hash_table.capacity)
    if hash_table.storage[hashkey] == None:
        hash_table.storage[hashkey] = LinkedPair(key, value)
    else:
        tmp = hash_table.storage[hashkey]
        if tmp.key == key:
            hash_table.storage[hashkey].value = value
        else:
            while tmp.next != None:
                tmp = tmp.next
                if tmp.key == key:
                    tmp.value = value
                    return None
        tmp.next = LinkedPair(key, value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    key_hash = hash(key, hash_table.capacity)
    if hash_table.storage[key_hash] == None:
        print('That key does not exist')
    else:
        existing_node = hash_table.storage[key_hash]
        last_node = None
        while existing_node and existing_node.key != key:
            last_node = existing_node
            existing_node = last_node.next
        if last_node:
            last_node.next = existing_node.next
        else:
            hash_table.storage[key_hash] = existing_node.next

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    key_hash = hash(key, hash_table.capacity)
    current_node = hash_table.storage[key_hash]
    while current_node:
        if current_node.key == key:
            return current_node.value
        else:
            current_node = current_node.next
    return None

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_capacity = 2 * hash_table.capacity
    new_table = HashTable(new_capacity)
    for i in range(len(hash_table.storage)):
        current_node = hash_table.storage[i]
        while current_node != None:
            hash_table_insert(new_table, hash_table.storage[i].key, hash_table.storage[i].value)
            current_node = current_node.next
    return new_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
