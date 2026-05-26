# Python - Serialization

## Description

This project explores marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. It covers how data can be transformed and communicated between different parts of a system, or even across different systems.

## What is Serialization?

Serialization involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal is to preserve the state of an object so it can be recreated in an identical state elsewhere.

## Learning Objectives

- Articulate the differences and similarities between marshaling and serialization
- Implement serialization in a practical programming task
- Understand how serialized data can be used in web applications, databases, and network communications
- Evaluate the performance implications of different serialization formats (JSON, XML, binary)

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use `pycodestyle` (version 2.7.*)
- All files must be executable

## Tasks

### 0. Basic Serialization — `task_00_basic_serialization.py`

A module with two functions:
- `serialize_and_save_to_file(data, filename)`: serializes a Python dictionary to a JSON file
- `load_and_deserialize(filename)`: deserializes a JSON file and returns a Python dictionary

### 1. Pickling Custom Classes — `task_01_pickle.py`

Serialization and deserialization of custom Python classes using the `pickle` module.

### 2. Converting CSV Data to JSON Format — `task_02_csv.py`

A function that reads a CSV file and converts its content to JSON format.

### 3. Serializing and Deserializing with XML — `task_03_xml.py`

Serialization and deserialization of data using XML format.

## Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-serialization`