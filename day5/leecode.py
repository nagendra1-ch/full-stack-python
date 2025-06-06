def fun(numBottles,numExchange):
        total_bottles=numBottles
        while numBottles>0:
            empty_bottles=numBottles
            numBottles=0
            numBottles+=empty_bottles//numExchange
            total_bottles+=empty_bottles//numExchange
        return total_bottles
            

        
print(fun(9,3))