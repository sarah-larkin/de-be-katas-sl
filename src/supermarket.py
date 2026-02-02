def queue_time(customers: list, checkouts: int) -> int:
    """calculate queue time

    Args:
        customers (list): list of postitive ints representing the queue, each int represents a customer and the value is the amount of time they require.
        checkouts (int): positve int, the number to checkout tills

    Returns:
        int: the amount of time for the queue to be cleared
    """
    #edge cases
    if not customers: 
        return 0 
    
    elif checkouts < 1: 
        raise ValueError("No Checkout")

    #option of multiple checkouts -> list 
    #next customer needs to be assigned to the lowest value checkout each time
    #find the total time for each checkout 

    checkout_list = [0] * checkouts # list of 0's for each checkout 
    #[0] * 3 == [0, 0, 0]

    #list.index(element, start, end) method 
    #returns the position at the first occurrence of the specified value.

    for customer in customers: 
        quickest_till_position = checkout_list.index(min(checkout_list))
        checkout_list[quickest_till_position] += customer
    
    return max(checkout_list)




#queue_time([2, 3, 10], 2)