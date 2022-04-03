#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:52:16 2022

@author: yamamotod
"""




def reversePrefix(word: str, ch: str) -> str:
        if ch not in word:
            return word
        return (''.join(reversed(word[:(word.index(ch)+1)]))+word[(word.index(ch))+1:])
      
        



def reversePrefix2(word, ch):
	i = word.find(ch)
	# find method of string returns -1 if ch is not present in string
	if i != -1:
	  new_word = word[i::-1]
	  new_word += word[i+1:]

	  return new_word
	else:
	  return word       
        
print(reversePrefix("abcdefd",'d'))        
print(reversePrefix2("abcdefd",'d'))    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
#    
#    Input: word = "abcdefd", ch = "d"
#Output: "dcbaefd"