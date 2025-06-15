# Heap Data Structures Assignment 4

## Overview
This repository contains the implementation, analysis, and applications for **Assignment 4: Heap Data Structures**. The project focuses on:
- **Heapsort**: An efficient O(n log n) sorting algorithm using a max-heap.
- **Priority Queue**: A max-heap-based priority queue for task scheduling, supporting insert, extract_max, update_priority, and is_empty operations.
- **Empirical Comparison**: Performance comparison of Heapsort with Quicksort and Merge Sort across various input sizes and distributions.
- **Task Scheduler Simulation**: Demonstrates the priority queue's application in scheduling tasks based on priority.

The implementations are written in Python, thoroughly analyzed for time and space complexity, and documented in a detailed report.

## Repository Structure
- `assignment4.py`: Python source code containing Heapsort, Priority Queue, sorting algorithm comparisons, and task scheduler simulation.
- `Report Assignment4.pdf`: PDF source for the project report, detailing design choices, implementation, analysis, and results.
- `README.md`: This file, providing project overview, setup instructions, and summary.

## Setup and Running Instructions
1. **Prerequisites**:
   - Python 3.6 or higher (no external libraries required; uses standard `time` and `random` modules).
   - For the report: LaTeX installation (e.g., TeX Live) or Overleaf for compiling `Heap_Report.tex`, and Pandoc or a PDF-to-Word converter for .docx output.
2. **Steps**:
   - Clone the repository:
     ```bash
     git clone https://github.com/mohitmurali/MSCS532_Assignment4
     ```
   - Navigate to the repository directory:
     ```bash
     cd MSCS532_Assignment4
     ```
   - Run the Python code:
     ```bash
     python3 assignment4.py
     ```
   - Output:
     - Heapsort result on a sample array.
     - Performance comparison of Heapsort, Quicksort, and Merge Sort for input sizes 100, 1000, and 10,000 (random, sorted, reverse-sorted distributions).
     - Task scheduler simulation output showing task execution order based on priority.
  
## Summary of Findings
- **Heapsort Implementation**:
  - Efficient O(n log n) time complexity, in-place with O(1) space.
  - Handles edge cases (empty arrays, single elements, duplicates, large inputs).
  - Well-documented with docstrings and inline comments.
- **Priority Queue Implementation**:
  - Max-heap-based, with O(log n) for insert, extract_max, and update_priority; O(1) for is_empty.
  - Uses a dictionary for O(1) task lookup, enhancing efficiency.
  - Handles edge cases (empty queue, invalid task IDs, single tasks).
- **Empirical Comparison**:
  - Tested on input sizes 100, 1000, 10,000 with random, sorted, and reverse-sorted distributions.
  - Heapsort: Consistent O(n log n) performance.
  - Quicksort: Fastest average-case with median-of-three pivot, but sensitive to input.
  - Merge Sort: Stable O(n log n), but requires O(n) space.
- **Task Scheduler Simulation**:
  - Demonstrates dynamic task scheduling, prioritizing higher-priority tasks.
  - Example output shows correct execution order based on task priority and arrival time.
- **Report**:
  - Comprehensive APA 7-formatted document covering design choices, implementation details, time complexity analysis, and empirical results.
  - Includes edge case analysis and discussion of heap size impact on performance.

