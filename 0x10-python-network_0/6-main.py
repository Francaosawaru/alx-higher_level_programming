#!/usr/bin/python3
"""
Defines a peak-finding algorithm
"""

 # Corrected import statement
 from importlib import import_module

 # Dynamic import of find_peak function from 6-peak.py
 peak_module = import_module('6-peak')
 find_peak = peak_module.find_peak

 # Test function for find_peak
 def test_find_peak():
     """
         Test function for find_peak
             """
                 peak = find_peak([1, 2, 4, 6, 3])
                     print(peak)  # Example output: 6

                     # Execute the test function
                     if __name__ == "__main__":
                         test_find_peak()

