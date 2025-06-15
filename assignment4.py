import time
import random

# Heapsort Implementation
def heapify(arr, n, i):
    """Maintain max-heap property at index i for array of size n."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    """Convert array into a max-heap."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    """Sort array using Heapsort algorithm. Time: O(n log n), Space: O(1)."""
    if len(arr) <= 1:  # Handle edge cases
        return
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Extract max
        heapify(arr, i, 0)

# Quicksort Implementation (Improved with Median-of-Three)
def median_of_three(arr, low, high):
    """Select pivot as median of first, middle, last elements."""
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def quicksort(arr, low=0, high=None):
    """Sort array using Quicksort with median-of-three pivot. Time: O(n log n) average."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = median_of_three(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Merge Sort Implementation
def merge_sort(arr):
    """Sort array using Merge Sort. Time: O(n log n), Space: O(n)."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Empirical Comparison
def compare_sorting_algorithms():
    """Compare Heapsort, Quicksort, and Merge Sort on various input sizes and distributions."""
    sizes = [100, 1000, 10000]
    distributions = ["random", "sorted", "reverse"]
    for size in sizes:
        print(f"\nSize: {size}")
        for dist in distributions:
            if dist == "random":
                arr = random.sample(range(size), size)
            elif dist == "sorted":
                arr = list(range(size))
            else:  # reverse
                arr = list(range(size, 0, -1))
            
            arr_heap = arr.copy()
            arr_quick = arr.copy()
            arr_merge = arr.copy()
            
            start = time.time()
            heapsort(arr_heap)
            heap_time = time.time() - start
            
            start = time.time()
            quicksort(arr_quick)
            quick_time = time.time() - start
            
            start = time.time()
            merge_sort(arr_merge)
            merge_time = time.time() - start
            
            print(f"{dist.capitalize()} - Heapsort: {heap_time:.4f}s, Quicksort: {quick_time:.4f}s, Merge Sort: {merge_time:.4f}s")

# Priority Queue Implementation
class Task:
    """Represents a task with ID, priority, and arrival time."""
    def __init__(self, task_id, priority, arrival_time):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time

class PriorityQueue:
    """Max-heap based priority queue for task scheduling."""
    def __init__(self):
        self.heap = []  # List-based max-heap
        self.index_map = {}  # Maps task_id to heap index

    def _swim(self, index):
        """Move task at index up to maintain max-heap property."""
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent].priority:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _sink(self, index):
        """Move task at index down to maintain max-heap property."""
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < n and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < n and self.heap[right].priority > self.heap[largest].priority:
                largest = right
            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        """Swap tasks at indices i and j, updating index_map."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.index_map[self.heap[i].task_id] = i
        self.index_map[self.heap[j].task_id] = j

    def insert(self, task):
        """Insert a task into the heap. Time: O(log n)."""
        self.heap.append(task)
        index = len(self.heap) - 1
        self.index_map[task.task_id] = index
        self._swim(index)

    def extract_max(self):
        """Remove and return highest-priority task. Time: O(log n)."""
        if not self.heap:
            return None
        max_task = self.heap[0]
        last_task = self.heap.pop()
        if self.heap:
            self.heap[0] = last_task
            self.index_map[last_task.task_id] = 0
            self._sink(0)
        del self.index_map[max_task.task_id]
        return max_task

    def update_priority(self, task_id, new_priority):
        """Update task priority and adjust heap. Time: O(log n)."""
        if task_id not in self.index_map:
            return
        index = self.index_map[task_id]
        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority
        if new_priority > old_priority:
            self._swim(index)
        elif new_priority < old_priority:
            self._sink(index)

    def is_empty(self):
        """Check if queue is empty. Time: O(1)."""
        return len(self.heap) == 0

# Task Scheduler Simulation
def scheduler_simulation(tasks):
    """Simulate priority-based task scheduling."""
    pq = PriorityQueue()
    current_time = 0
    tasks.sort(key=lambda x: x.arrival_time)
    task_index = 0
    print("\nScheduler Simulation:")
    while task_index < len(tasks) or not pq.is_empty():
        while task_index < len(tasks) and tasks[task_index].arrival_time <= current_time:
            pq.insert(tasks[task_index])
            task_index += 1
        if not pq.is_empty():
            task = pq.extract_max()
            print(f"Time {current_time}: Running Task {task.task_id} (Priority: {task.priority})")
        current_time += 1

# Example Usage
if __name__ == "__main__":
    # Heapsort Test
    arr = [12, 11, 13, 5, 6, 7]
    heapsort(arr)
    print("Heapsort Result:", arr)
    
    # Compare Sorting Algorithms
    compare_sorting_algorithms()
    
    # Scheduler Simulation Test
    tasks = [
        Task(1, 3, 0),
        Task(2, 5, 1),
        Task(3, 2, 0),
        Task(4, 4, 2)
    ]
    scheduler_simulation(tasks)