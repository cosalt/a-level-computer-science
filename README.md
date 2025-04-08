# A-Level Computer Science Revision Guide (Programming bit)

This repository contains the essential concepts and algorithms required for A-level Computer Science, focusing on data structures, algorithms, and core programming concepts.

## Table of Contents

- [Data Structures](#data-structures)
  - [Linked List](#linked-list)
  - [Binary Tree](#binary-tree)
  - [Stack](#stack)
  - [Queue](#queue)
- [Algorithms](#algorithms)
  - [Sorting Algorithms](#sorting-algorithms)
    - [Insertion Sort](#insertion-sort)
    - [Bubble Sort](#bubble-sort)
  - [Search Algorithms](#search-algorithms)
    - [Binary Search](#binary-search)
    - [Linear Search](#linear-search)
- [Core Programming Concepts](#core-programming-concepts)
  - [Recursion](#recursion)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Working with Files](#working-with-files)
  - [Text Files](#text-files)

---

## Data Structures

### Linked List

A linked list is a linear data structure where each element (node) points to the next node in the sequence. It consists of a collection of nodes where each node contains a data field and a reference (or link) to the next node.

- **Singly Linked List**: Each node points to the next node.
- **Doubly Linked List**: Each node has links to both the next and the previous nodes.

### Binary Tree

A binary tree is a hierarchical structure where each node has at most two children, often referred to as the left and right children. Binary trees are used to implement efficient searching and sorting algorithms.

- **Types of Binary Trees**:
  - Full Binary Tree
  - Complete Binary Tree
  - Balanced Binary Tree
  - Binary Search Tree (BST)

### Stack

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. Operations on a stack include:
- **Push**: Adds an item to the stack.
- **Pop**: Removes the top item from the stack.
- **Peek**: Returns the top item without removing it.

### Queue

A queue is a linear data structure that follows the First In, First Out (FIFO) principle. Operations include:
- **Enqueue**: Adds an item to the end of the queue.
- **Dequeue**: Removes the item from the front of the queue.
- **Peek**: Returns the front item without removing it.

---

## Algorithms

### Sorting Algorithms

#### Insertion Sort

Insertion sort works by building a sorted portion of the list one element at a time. It compares each element with the already sorted portion and inserts it into the correct position.

**Time Complexity**: 
- Best Case: O(n)
- Worst Case: O(n<sup>2</sup>)

#### Bubble Sort

Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until no swaps are needed.

**Time Complexity**: 
- Best Case: O(n)
- Worst Case: O(n<sup>2</sup>)

### Search Algorithms

#### Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list by repeatedly dividing the search interval in half. If the value is less than the middle element, the search continues in the left half, and if greater, it continues in the right half.

**Time Complexity**: O(log n)

#### Linear Search

Linear search is a simple search algorithm that checks each element in the list sequentially until the desired item is found.

**Time Complexity**: O(n)

---

## Core Programming Concepts

### Recursion

Recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem. A function is defined in terms of itself.

**Base Case**: The condition that stops the recursion.
**Recursive Case**: The part where the function calls itself.

### Object-Oriented Programming (OOP)

OOP is a programming paradigm based on the concept of "objects," which can contain data and methods. The core principles of OOP are:
- **Encapsulation**: Bundling data and methods that operate on that data.
- **Inheritance**: A class can inherit properties and methods from another class.
- **Polymorphism**: The ability of different objects to respond to the same method call in different ways.
- **Abstraction**: Hiding the complex implementation details and showing only the essential features of the object.

---

## Working with Files

### Text Files

Text files are used to store plain text. Common operations with text files include:
- **Opening a file**: Opening a file for reading, writing, or appending.
- **Reading from a file**: Retrieving data from a file.
- **Writing to a file**: Writing data to a file.
- **Closing a file**: Ensuring the file is properly closed after operations are completed.

---

## License

This repository is for educational purposes only. You are free to use and push the content as you revise for your A-level Computer Science exam.

