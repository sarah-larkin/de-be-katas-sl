# find index of the nth closing brackets
# n = location of opening bracket

def find_closing_parenthesis(phrase: str, n: int): 
    if not phrase or n < 0 :
        return -1
    
    count_open = 0 
    parenthesis_depth = 0

    for idx, char in enumerate(phrase): 
        if char == "(": 
            count_open += 1                         #count opening brackets until they match n
    
            if count_open == n:                     #starting point
                parenthesis_depth = 1               #first ( already captured here 
            elif parenthesis_depth > 0:             #later iterations 
                parenthesis_depth += 1

        elif char == ")" and parenthesis_depth > 0: #only checking ) once depth > 0 --> original loop!! 
            parenthesis_depth -= 1                  #close nested brackets 
 
            if parenthesis_depth == 0:              #once bracket closed
                return idx
    return -1





            
            



# The index() method returns the position at the first occurrence of the 
# specified value.

# list.index(elmnt, start, end)



#initial attempts

#    if not phrase or not n:
#         return -1
    
    # if n == 1: 
    #     return phrase.index(")")
    
    # if n > 0: 
    #     count_opening = 0
    #     count_closing = 0
    #     for idx, letter in enumerate(phrase): 
    #         if letter == "(":
    #             count_opening += 1
    #         if letter == ")": 
    #             count_closing +=1
    #         if letter == ")" and count_opening == n: 
                # return idx
            
    # if n > 0:
    #     count_open = 0
    #     parenthesis = 0
  
    #     for idx, letter in enumerate(phrase): 
    #         if letter == "(": 
    #             count_open += 1
    #             if count_open == n:
    #                 parenthesis += 1
    #                 if letter == ")": 
    #                     parenthesis -= 1
    #                 if parenthesis == 0: 
    #                     return idx