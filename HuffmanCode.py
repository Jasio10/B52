# Function that takes a string as a argument, creates "Huffman code" for that string and return the indicator
# whether "Huffman code" would be shorter then original string
#  Huffman code example: “aaabbc” -> “a3b2c1"
def ReadData():
    the_data = input("Input string: ")
    if len(the_data) > 0:
        print("Your string :", the_data)
    else:
        print("Invalid entry")
        exit()
    return the_data

def CalculateProbability(the_data):
    the_symbols = dict()
    for item in the_data:
        if the_symbols.get(item) == None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols
def Encoding(the_data):
    symbolWithProbs = CalculateProbability(the_data)

    stringEncoded = ''
    for x, y in symbolWithProbs.items():
        stringEncoded += (str(x))
        stringEncoded += (str(y))
        print("Character:", str(x)," Occurrence:", str(y))

    print()
    print("Coded string : ", stringEncoded)
    return stringEncoded

def Indicator(the_data, stringEncoded):
    indicator = None
    if len(stringEncoded) < len(the_data):
        indicator = True
    else:
        indicator = False
    return indicator

the_data = ReadData()
indicator = Indicator(the_data, Encoding(the_data))
print("Indicator if encoded string is shorter then original :", indicator)