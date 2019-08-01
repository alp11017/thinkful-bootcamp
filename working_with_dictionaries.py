
#problem statement https://www.codewars.com/kata/thinkful-dictionary-drills-order-filler/train/python

#my solution

def fillable(stock, merch, n):
    if (merch in stock) and stock[merch]-n >=0:
        return True
    else:
        return False

#codewars solution
    
def fillable(stock, merch, n):
  return stock.get(merch, 0) >= n

#----------------
#problem statement https://www.codewars.com/kata/thinkful-dictionary-drills-user-contacts/train/python
    
#my solution
    
def user_contacts(data):
    dictionary_data = {}
    for i in data:
        try: 
            dictionary_data[i[0]] = i[1]
        except:
            dictionary_data[i[0]] = None
    return dictionary_data

#codewars solution

def user_contacts(data):
    return {contact[0]: contact[1] if len(contact) > 1 else None
            for contact in data}

#----------------

#problem statement https://www.codewars.com/kata/thinkful-dictionary-drills-multiple-modes

#my attempt (did not solve)

def modes(data):
    counts = []
    mode = [] 
    for i in data:
        appearances = int(data.count(i))
        counts.append(appearances)
    if len(counts) <= 1 or (counts[0] == counts[-1]):
        return mode
    else:
        if data.count(i) == max(counts):
            mode.append(i)
        return mode

#codwars solution

def modes(data):
    frequency = {}
    mode_list = []
    
    # adds or creates a counter for each character
    for d in data:
        if d in frequency:
            frequency[d] += 1
        else:
            frequency[d] = 1
    
    # adds modes from the dictionary to a list, and checks that there is a mode
    for f in frequency:
        if frequency[f] == max(frequency.values()) > min(frequency.values()):
            mode_list.append(f)
            
    return sorted(mode_list)



