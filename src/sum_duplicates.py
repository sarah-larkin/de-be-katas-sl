
def sum_consecutive_duplicates(num_list): 
    temp_list = []
    output = []
    for num in num_list: 
        #appending to tempt list to collect duplicate 
        if len(temp_list) == 0 or num in temp_list: #if temp_list is empty or num is in temp_list
            temp_list.append(num)
        #if not matching
        else: 
            output.append(sum(temp_list))
            temp_list = [num] # simpler override of temp_list
    #after for loop completed
    if temp_list: 
        output.append(sum(temp_list)) #for final iteration

    return output


def reduce_consecutives(num_list): 
    latest_list = sum_consecutive_duplicates(num_list)

    #base case
    if latest_list == num_list: 
        return latest_list

    return reduce_consecutives(latest_list) #call current function with variable calling original function

#base case
#latest list = num_list with duplicates summed/removed
#if latest_list == num_list is means there are no more duplicates so return here




