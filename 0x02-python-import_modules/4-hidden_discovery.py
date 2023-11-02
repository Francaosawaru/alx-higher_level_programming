#!/usr/bin/python3

if _name_ == "_main_":
import hidden_4
for variable in dir(hidden_4):
if variable[0] != '__' and variable[1] != '_':
print(variable)
