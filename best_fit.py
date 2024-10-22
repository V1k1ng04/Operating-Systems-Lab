# Dynamic Storage Allocation Strategy

class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.is_allocated = False

class MemoryManager:
    def __init__(self):
        self.memory_blocks = []

    def add_memory_block(self, size):
        self.memory_blocks.append(MemoryBlock(size))

    def first_fit(self, request_size):
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= request_size:
                block.is_allocated = True
                return f"Allocated {request_size} units using First Fit."
        return "No suitable block found for First Fit."

    def best_fit(self, request_size):
        best_block = None
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= request_size:
                if best_block is None or block.size < best_block.size:
                    best_block = block
        if best_block:
            best_block.is_allocated = True
            return f"Allocated {request_size} units using Best Fit."
        return "No suitable block found for Best Fit."

# Example Usage
if __name__ == "__main__":
    memory_manager = MemoryManager()
    memory_manager.add_memory_block(100)
    memory_manager.add_memory_block(200)
    memory_manager.add_memory_block(300)

    print(memory_manager.first_fit(150))
    print(memory_manager.best_fit(80))
    print(memory_manager.first_fit(50))
    print(memory_manager.best_fit(250))
