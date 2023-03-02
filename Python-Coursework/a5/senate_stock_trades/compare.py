from senate_stock_trades import util as u

def count_diff(first_senator_name, second_senator_name):
    # integers for incrementing number of times senator name has appeared 
    first_count_of_transaction = 0
    second_count_of_transaction = 0
    
    # Iterate through list elements
    for i, value in enumerate(u.get_data()):
        # if the first senator name is in data
        if u.get_data()[i]['senator'] == first_senator_name:
            first_count_of_transaction = first_count_of_transaction + 1 # increment 
        
        # if second senator name is in data
        if u.get_data()[i]['senator'] == second_senator_name:
            second_count_of_transaction = second_count_of_transaction + 1 # increment
            
    #return the count difference of the first and second senator names that appeared  
    return(first_count_of_transaction - second_count_of_transaction)
    
def amount_diff(first_senator_name, second_senator_name):
    #create a dictionary
    range_of_senator = {}

    # Iterate through list elements
    for key, value in enumerate(u.get_data()):
        # if first senator name is in data
        if u.get_data()[key]['senator'] == first_senator_name:
        
            # if senator is not in dictionary
            if u.get_data()[key]['senator'] not in range_of_senator:
                # do not increment 
                range_of_senator[u.get_data()[key]['senator']] = (u.get_data()[key]['amount_range'][0], u.get_data()[key]['amount_range'][1])
            
            # else add amount ranges
            else:
                range_of_senator[u.get_data()[key]['senator']] = u.add_amount_ranges(range_of_senator[u.get_data()[key]['senator']], u.get_data()[key]['amount_range'])
           
        # if second senator name is in data
        if u.get_data()[key]['senator'] == second_senator_name:
        
            # if senator name is not in dictionary
            if u.get_data()[key]['senator'] not in range_of_senator:
                # do not increment
                range_of_senator[u.get_data()[key]['senator']] = (u.get_data()[key]['amount_range'][0], u.get_data()[key]['amount_range'][1])
            
            # else add amount ranges
            else:
                range_of_senator[u.get_data()[key]['senator']] = u.add_amount_ranges(range_of_senator[u.get_data()[key]['senator']], u.get_data()[key]['amount_range'])
    
    # return the range difference of first and second senator name
    return(u.sub_amount_ranges(range_of_senator[first_senator_name], range_of_senator[second_senator_name]))