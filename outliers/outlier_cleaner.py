#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    residuals = predictions - net_worths
    for i in range(0, len(residuals)):
        tuple = (ages[i][0], net_worths[i][0], residuals[i][0])
        cleaned_data.append(tuple)

    remove_count = int(round(len(cleaned_data) - (len(cleaned_data) * 0.9)))   
    ordered_list = sorted(cleaned_data, key=lambda t: t[2], reverse=True)

    print "clean before: ", len(cleaned_data)

    for i in range(0, remove_count):
        tuple = ordered_list[i]
        cleaned_data.remove(tuple)

    print "clean after: ", len(cleaned_data)
    
    return cleaned_data

