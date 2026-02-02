def queue_time(customers: list, checkouts: int) -> int:
    """calculate queue time

    Args:
        customers (list): list of postitive ints representing the queue, each int represents a customer and the value is the amount of time they require.
        checkouts (int): positve int, the number to checkout tills

    Returns:
        int: the amount of time for the queue to be cleared
    """
    
    if len(customers) == 0: 
        return 0 
    
    elif checkouts < 1: 
        return "error"

    elif checkouts == 1: 
        return sum(customers)

    elif len(customers) == checkouts:
        return max(customers)

    elif checkouts == 2: 
        checkout1 = []
        checkout2 = []

        for i in range(len(customers)): 
            if i == 0: 
                checkout1.append(customers[i])
            elif i % 2 == 0: 
                checkout1.append(customers[i])
            else: checkout2.append(customers[i])

        checkout1_total = sum(checkout1)
        checkout2_total = sum(checkout2)

        if checkout1_total > checkout2_total: 
            return checkout1_total
        else: return checkout2_total

