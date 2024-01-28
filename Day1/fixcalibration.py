#!/usr/bin/env python3
#Advent of Code 2023 Day 1
#Program to clean up calibration data. Will pull numerical digits from string
#Combines first and last digits of each line to a two digit number
#Calculates sum of all two digit numbers

def read_file(): #function to read input and remove data that is not numeric
    input_file=open('input.txt','r')
    file=input_file.readlines() #read lines from file to list
    return(file)

def clean_digits(): #function to remove non numerical characters from input
    clean = [] #Initiates list to store numbers
    for i in convert_letters(): #Iterates through input list
        digits_only = ''.join(j for j in i if j.isdigit()) #replaces non digits with empty string
        if digits_only:
            clean.append((digits_only))
    return(clean)

def recover_value(): #function to combine first and last digit
    string_digit=[] 
    two_digit=[] #list to store combined digits
    for i in clean_digits(): #iterate through each element of list
            string_digit.append(i[0] + i [-1]) #add the first and last digits to list
    for k in string_digit:
        two_digit.append(int(k)) #convert list to int
    return two_digit

def sum_calibrations():
    total_sum=sum(recover_value())
    return total_sum
        
def convert_letters():
    letter_key={'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    formatted=[]
    for i in read_file():
        new_string = i
        for substring, replacement in letter_key.items():
            if substring in new_string:
                new_string = new_string.replace(substring, replacement)
        formatted.append(new_string)
    return formatted


if __name__ == "__main__":
    read_file()
    convert_letters()
    clean_digits()
    recover_value()
    sum_calibrations()
    #print(read_file())
    #print(convert_letters())
    print(clean_digits())
    print(recover_value())
    print(sum_calibrations())
    