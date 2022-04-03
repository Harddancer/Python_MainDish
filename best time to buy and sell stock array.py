#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def max_profit(prices)-> int:
          
        if not prices:
            return 0
        
        maxx = 0
        minn = prices[0]
        
        for price in prices[1:]:            
            profit = price - minn
            maxx = max(maxx, profit)
            minn = min(minn, price)
        return maxx
            
print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,5,1]))