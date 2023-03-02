from senate_stock_trades import util as u

def count_trades(ticker_symbol):
    # Create a dictionary
    count_of_trades = {}

    # Iterate through list elements
    for key, value in enumerate(u.get_data()):
        # if ticker has ticker symbol
        if u.get_data()[key]['ticker'] == ticker_symbol:
            
            # if senator does not have types then do not increment
            if u.get_data()[key]['senator'] not in count_of_trades:
                count_of_trades[u.get_data()[key]['senator']] = 1
            
            # else senator does have types then increment
            else:
                count_of_trades[u.get_data()[key]['senator']] += 1
                
    return(count_of_trades) 
    
def sum_trades(ticker_symbol):
    
    range_of_trade = {}

    # Iterate through list elements
    for key, value in enumerate(u.get_data()):
        # if ticker has ticker symbol
        if u.get_data()[key]['ticker'] == ticker_symbol:
        
            # if senator does not have ticker then do not increment
            if u.get_data()[key]['senator'] not in range_of_trade:
                 range_of_trade[u.get_data()[key]['senator']] = (u.get_data()[key]['amount_range'][0], u.get_data()[key]['amount_range'][1])
            
            # else add amount ranges
            else:
                range_of_trade[u.get_data()[key]['senator']] = u.add_amount_ranges(range_of_trade[u.get_data()[key]['senator']], u.get_data()[key]['amount_range'])
                
    return(range_of_trade)