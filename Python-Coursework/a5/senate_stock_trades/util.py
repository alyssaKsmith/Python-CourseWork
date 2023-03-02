def get_data():
    import os
    import json
    
    # get path of json file 
    fname = os.path.join(os.path.dirname(__file__), 'senate-stock-trades.json')
    # open and load the data from json file 
    data = json.load(open(fname))
    
    return data

def add_amount_ranges(lower_bound, upper_bound):
    # if amount range upper or lower bound has value of None
    if lower_bound[1] == None or upper_bound[1] == None:
        # return upper as None
        return(lower_bound[0] + upper_bound[0], None)
    # else add    
    else:
        return(lower_bound[0] + upper_bound[0], lower_bound[1] + upper_bound[1])

    
def sub_amount_ranges(lower_bound, upper_bound):
    # if amount range upper or lower bound has value of None
    if lower_bound[1] == None or upper_bound[1] == None:
        # return upper as None
        return(lower_bound[0] - upper_bound[0], None)
    # else subtract
    else:
        return(lower_bound[0] - upper_bound[0], lower_bound[1] - upper_bound[1])