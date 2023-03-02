# import files
from senate_stock_trades import util 
from senate_stock_trades import ticker 
from senate_stock_trades import compare

import sys

# if argument is ticker and the length is three 
if sys.argv[1] == 'ticker' and len(sys.argv) == 3:
    arg = sys.argv[2]s
    # call count trades and print 
    ticker_analysis_count = ticker.count_trades(arg)
    print("Number of trades:", ticker_analysis_count)
    #call sum of trades and print
    ticker_analysis_sum = ticker.sum_trades(arg)
    print("Sum of trade values:", ticker_analysis_sum)
# else if it is compare and length of four
elif sys.argv[1] == 'compare' and len(sys.argv) == 4:
    arg1 = sys.argv[2]
    arg2 = sys.argv[3]
    # call count difference and amount difference
    compare_transaction = compare.count_diff(arg1, arg2)
    compare_amount_transaction = compare.amount_diff(arg1, arg2)
    # if count difference is less than zero
    if(compare_transaction < 0):
        # value is a negative
        print(arg1, "has", compare_transaction, "trades with value", compare_amount_transaction, "than", arg2)
        
    else:
        # else the value is a positive
        print(arg1, "has +", compare_transaction, "trades with value", compare_amount_transaction, "than", arg2)
# else print usage message  
else:
    print("Usage: python analyze_trades.py [ticker <ticker> | compare <senator1> <senator2>]")