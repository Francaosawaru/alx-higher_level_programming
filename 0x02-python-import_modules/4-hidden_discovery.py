#!/usr/bin/python3

if _name_ == "_main_":
    """print all names defined by hidden_4 module."""
import hidden_4
# Print sorted name from directory
for names =dir(hidden_4)
if name[:2] != '__':
print("{}".format(name))
