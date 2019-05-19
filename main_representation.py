# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:19:10 2019

@author: ning.shi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:33:05 2019

@author: ning.shi
"""
import numpy as np
from random import choice
from pyknow import *

PRICE_bought=50
PRICE_high=50*1.3
PRICE_low=50*0.8

class Price(Fact):
    pass

class StockTrade(KnowledgeEngine):
    @Rule(NOT(Fact(x=W())))
    def init(self):
 #       self.declare(Fact(x=50))
         pass
    

    @Rule(Fact(x=P(lambda x: x >= PRICE_low) & P(lambda x: x <= PRICE_high)))
    def pr(self):
        print("the price is between low and high value, hold the stock") 
     
    
    @Rule(Fact(x=P(lambda x: x > PRICE_high)))
    def ph(self):
        print("the price is increase by more than 20%, sell the stock ")
        self.retract(0)
 #       self.declare(Fact(x=50))
         
    @Rule(Fact(x=P(lambda x: x < PRICE_low)))
    def pl(self):
        print("the value is less than 50, sell the stock to lock the lost") 
    
        
engine = StockTrade()
engine.reset()
engine.declare(Fact(x=60))
engine.run() 
