def fifo(ref_string, frames):
    memory = []
    faults = 0
    for page in ref_string:
        if page not in memory:
            faults += 1
            if len(memory) == frames:
                memory.pop(0)  # Evict oldest
            memory.append(page)
    return faults

def lru(ref_string, frames):
    memory = []
    faults = 0
    for page in ref_string:
        if page not in memory:
            faults += 1
            if len(memory) == frames:
                memory.pop(0)  # Evict least recently used
            memory.append(page)
        else:
            # Move hit page to the back to mark it as most recently used
            memory.remove(page)
            memory.append(page)
    return faults

def second_chance(ref_string, frames):
    memory = []
    bits = []
    ptr = 0
    faults = 0
    for page in ref_string:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
                bits.append(1)
            else:
                while True:
                    if bits[ptr] == 0:
                        memory[ptr] = page
                        bits[ptr] = 1
                        ptr = (ptr + 1) % frames
                        break
                    else:
                        bits[ptr] = 0
                        ptr = (ptr + 1) % frames
        else:
            idx = memory.index(page)
            bits[idx] = 1
    return faults

ref_string = [1, 4, 6, 8, 2, 3, 5, 6, 2, 1]
print("3 Frames -> FIFO:", fifo(ref_string, 3), " LRU:", lru(ref_string, 3), " SC:", second_chance(ref_string, 3))
print("4 Frames -> FIFO:", fifo(ref_string, 4), " LRU:", lru(ref_string, 4), " SC:", second_chance(ref_string, 4))
