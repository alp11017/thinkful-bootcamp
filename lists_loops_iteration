#Complete the function that takes one argument, a list of words, and returns the length of the longest word in the list.
# https://www.codewars.com/kata/thinkful-list-drills-longest-word

#my code
#not sure why this piece of code wasn't working.

def longest(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
        return longest

#codewars solution

def longest(words):
    return max(map(len, words))

#-----------------------------------

#problem statement https://www.codewars.com/kata/thinkful-list-and-loop-drills-grade-calculator
#my solution

def calculate_grade(scores):
    grade = 0
    for score in scores:
        grade = grade + score
        average = grade/len(scores)
    if 90 <= average <= 100: return "A"
    if 80 <= average < 90: return "B"
    if 70 <= average < 80: return "C"
    if 60 <= average <70: return "D"
    else: return "F"


#codewars solution

def calculate_grade(scores):
    for score in scores:
        mean = sum(scores)/len(scores)
        if mean >= 90 and mean <= 100:
            return "A"
        elif mean >= 80 and mean < 90:
            return "B"
        elif mean >= 70 and mean < 80:
            return "C"
        elif mean >= 60 and mean < 70:
            return "D"
        else:
            return "F"

#-----------------------------------

#problem statement https://www.codewars.com/kata/thinkful-list-and-loop-drills-lists-of-lists


#my solution

def process_data(data):
    sums = []
    total = 1
    
    for i in data:
        difference = i[0] - i[1]
        sums.append(difference)
    
    for sum in sums:
        total *= sum
    return total

#code wars solution

def process_data(data):
    r = 1
    for d in data:
        r *= d[0] - d[1]
    return r

#-----------------------------------


# problem statement https://www.codewars.com/kata/thinkful-list-and-loop-drills-inverse-slicer/train/python

#my solution

def inverse_slice(items, a, b):
    del items[a:b]
    return items

#code wars solution

def inverse_slice(items, a, b):
    return items[:a] + items[b:]




