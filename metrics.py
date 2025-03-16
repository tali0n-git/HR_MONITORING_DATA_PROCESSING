


def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    average = 0
    
    for i in data:
        average += i

    if len(data) == 0:
        return([])

    average = average / len(data)

    return(round(average, 2))

def maximum(data: list) -> float:
    """
    Returns the maximum value in list of integers

    Args:
        data (list[int]): list of integers
    Returns:
        int: maximum number in the list
        OR
        list: empty list if an empty list is input
    """
    max_num = 0

    for i in data:
        if i >= max_num:
            max_num = i
    
    if max_num == 0:
        return([])

    return max_num


def variance(data: list) -> float:
    """
    Calculates population variance of a list og integers.

    Args:
        data (list[int]): list of integers
    Returns:
        int: population variance of the list
    """

    if (len(data) <= 1):
        return(data)


    avg = average(data)
    deviations = []
    sum_deviations = 0
    final_var = 0

    for i in data:
        deviations.append((i - avg)**2)                 #creating a list of squared deviations

    for i in deviations:
        sum_deviations += i

    final_var = sum_deviations / (len(data))            #calculating population variance

    return(final_var)


def standard_deviation(data: list) -> float:
    """
    Calculates the population standard deviation of a list of integers

    Args:
        data (list[int]): list of integers
    Returns:
        float: population standard deviation of the list (rounded to two decimal places)
    """

    if len(data) <= 1:
        return(data)

    stdev = round((variance(data))**(0.5), 2)

    return(stdev)
