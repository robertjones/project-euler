w0to19 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
          "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
          "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
wtens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
         "eighty", "ninety"]

# "one" + "hundred", "one" + "hundred" + "and" + "one"

# 0-20: fetch from dict

# 20-99: tens + units

# 100-999: hundreds + "hundred and" + 0-99

def num_to_words(x):
    hundreds = int(x/100)
    tens = int((x-hundreds*100)/10)
    units = int(x-hundreds*100-tens*10)

    hundreds_words = w0to19[hundreds] + ("hundred" if hundreds else "")
    joining =  "and" if hundreds and (tens or units) else ""
    tens_and_units_words = (wtens[tens] + w0to19[units] if tens >= 2 else
                            w0to19[tens*10 + units])
    
    return hundreds_words + joining + tens_and_units_words

w0to1000 = [num_to_words(x) for x in range(1000)] + ["onethousand"]

n0to1000 = [len(x) for x in w0to1000]

print(sum(n0to1000))