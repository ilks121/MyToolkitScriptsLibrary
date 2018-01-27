#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:18:18 2018

@author: ilkay
"""

def remChar(sString, sChar2Rem):
    # Initialise variables
    iLenStr = len(sString)
    iCount = 0
    sNewString = ""
    
    # Check if user has supplied empty string as the character to remove
    # As long as it is NOT an empty string then run the removal logic
    if sChar2Rem != "":
        
        # loop through each character in the string to check that was passed to the function
        while iCount <= iLenStr:
            
            # Identify character(s) in string to be tested against the removal
            # char(s). If the removal char(s) is multi char then the string to
            # identify will be the same length
            # Simultaneously, a separate variable to represent the single char
            # in the string to test is created so that the final output string
            # is rebuilt correctly and all section of the string are tested.
            sChar = sString[iCount:iCount+len(sChar2Rem)]
            sCharSingle = sString[iCount:iCount+1]
            
            # Rebuild string 1 character at a time as long as the character(s) do not match
            if sChar != sChar2Rem:
                
                sNewString = sNewString + sCharSingle
                iCount = iCount + 1
                
            else:
                
                # If the removal char(s) match then increment the count variable
                # used to traverse the string being tested so that the removal
                # char(s) are skipped
                iCount = iCount + len(sChar2Rem)
                
    else:
        
        # original string passed for testing is returned if the removal char(s)
        # passed is an empty string i.e. ""
        sNewString = sString
        
    # Return the final output from this function 
    return sNewString