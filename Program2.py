# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:11:59 2020

@author: giri
"""

def finding_longest_substring(string):
    sub_strings = dict()
    longest = 0
    current_length = 0
    
    
    for index,letter in enumerate(string):
        
        if(letter not in sub_strings):
            sub_strings[letter] = index
            current_length += 1
            if (current_length > longest):
                longest = current_length
            
        else:
            
            current_length = index - sub_strings[letter]
            sub_strings[letter] = index
            
    return longest


if __name__ == "__main__":
    string = str(input("Enter the input string to find its longest substring without repeatating chars : "))
    print("longest substring value without repeatating chars is '{}' among the input string is '{}' ".format(finding_longest_substring(string),string))
