
#You're writing code to control your town's traffic lights.
#You need a function to handle each change from green, to yellow,
#to red, and then to green again.
#Complete the function that takes a string as an argument representing
#the current state of the light and returns a string representing the
#state the light should change to.
#For example, update_light('green') should return 'yellow'.

#my solution

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    else:
        return "green"


#codewars solution

def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

#----------------------------

#Write a function take_umbrella() that takes two arguments: a string representing the current weather and a float representing the chance of rain today.
#Your function should return True or False based on the following criteria.
#You should take an umbrella if it's currently raining or if it's cloudy and the chance of rain is over 0.20.
#You shouldn't take an umbrella if it's sunny unless it's more likely to rain than not.
#The options for the current weather are sunny, cloudy, and rainy.
#For example, take_umbrella('sunny', 0.40) should return False.
#As an additional challenge, consider solving this kata using only logical operaters and not using any if statements.

#my attempt (did not solve completely)
#I was having a problem with sunny because I didn't include code for the portion where it said;
#You shouldn't take an umbrella if it's sunny unless it's more likely to rain than not.

def take_umbrella(weather, rain_chance):
    return ((weather == 'rainy') or (weather == 'cloudy' and rain_chance > 0.20)) or (weather == 'sunny')

#codewars solution

def take_umbrella(weather, rain_chance):
    # Your code here.
    return (weather=='cloudy' and rain_chance>0.20) or weather=='rainy' or (weather=='sunny' and rain_chance>0.5)

#----------------------------

#You like the way the Python + operator easily handles adding different numeric types, but you need a tool to do that kind of addition without killing your program with a TypeError exception whenever you accidentally try adding incompatible types like strings and lists to numbers.
#You decide to write a function my_add() that takes two arguments. If the arguments can be added together it returns the sum. If adding the arguments together would raise an error the function should return None instead.
#For example, my_add(1, 3.414) would return 4.414, but my_add(42, " is the answer.") would return None.
#Hint: using a try / except statement may simplify this kata.

#my solution

def my_add(a, b):
    try:
        return a+b
    except:
        return None

#Codewars solution
    def my_add(a, b):
    try:
        return a + b
    except TypeError:
        return None

#----------------------------
#You're playing a game with a friend involving a bag of marbles. In the bag are ten marbles:

#1 smooth red marble
#4 bumpy red marbles
#2 bumpy yellow marbles
#1 smooth yellow marble
#1 bumpy green marble
#1 smooth green marble
#You can see that the probability of picking a smooth red marble from the bag is 1 / 10 or 0.10 and the probability of picking a bumpy yellow marble is 2 / 10 or 0.20.
#The game works like this: your friend puts her hand in the bag, chooses a marble (without looking at it) and tells you whether it's bumpy or smooth. Then you have to guess which color it is before she pulls it out and reveals whether you're correct or not.
#You know that the information about whether the marble is bumpy or smooth changes the probability of what color it is, and you want some help with your guesses.
#Write a function color_probability() that takes two arguments: a color ('red', 'yellow', or 'green') and a texture ('bumpy' or 'smooth') and returns the probability as a decimal fraction accurate to two places.
#The probability should be a string and should discard any digits after the 100ths place. For example, 2 / 3 or 0.6666666666666666 would become the string '0.66'. Note this is different from rounding.
#As a complete example, color_probability('red', 'bumpy') should return the string '0.57'.

#my solution

def color_probability(color, texture):
    if texture == "smooth":
        probability = str(1/3)
        return probability[probability.find('.')-1:probability.find('.')+3]
    else:
        marbles = {"red" : 4, "yellow" : 2, "green" : 1}
        probability = str(marbles[color]/7)
        return probability[probability.find('.')-1:probability.find('.')+3]


#Codewars solution

def color_probability(color, texture):
    marbles = {"smooth": {"red": 1, "yellow": 1, "green": 1, "total": 3}, "bumpy": {"red": 4, "yellow": 2, "green": 1, "total": 7}}
    return "{}".format(marbles[texture][color] / marbles[texture]["total"])[:4]

#----------------------------

#problem statement https://www.codewars.com/kata/thinkful-logic-drills-hacking-p-hackers

#my solution

def categorize_study(p_value, requirements):
    satisfied_req = {6:1, 5:2, 4:4, 3:8, 2:16, 1:32, 0:64}
    bs_factor = satisfied_req[requirements]
    bs_level = p_value*bs_factor
    if requirements == 0 and bs_level < 0.05:
        return "Needs review"
    elif bs_level < 0.05:
        return "Fine"
    elif bs_level > 0.15:
        return "Pants on fire"
    else:
        return "Needs review"


#Codewars solution

def categorize_study(p_value, requirements):
    study_value = p_value * (2**(6-requirements))
    
    if study_value < 0.05 and requirements != 0:
        return "Fine"
    elif study_value < 0.05 and requirements == 0:
        return "Needs review"
    elif study_value > 0.05 and study_value < 0.15:
        return "Needs review"
    else:
        return "Pants on fire"

#----------------------------




