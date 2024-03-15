# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:34:31 2023

@author: lione
""


        
        n=int(input(""))

def is_a_vowel(char):
    return char in 'aeiou'

s = input()

current_len = 0
maximum_len = 0

for char in s:
    if is_a_vowel(char):
        current_len += 1
    else:
        maximum_len = max(maximum_len, current_len)
        current_len = 0

maximum_len = max(maximum_len, current_len)

print(maximum_len)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if x = 
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
    