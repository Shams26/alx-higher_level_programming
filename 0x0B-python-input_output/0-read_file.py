#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Opens a file and print it content to stdout (UTF8)."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")