"""
 Logic is we need to traverse the whole array and elements won't be repeated here.
 So we can take a temp array and index var which using which we can call recursively a func which keeps track of target value.
 Everytime we include the index value the target value is decreased then.
 Base condition will be to check the idx value and also if target values is 0.

 Here you can see the logic of backtracking is applied. 
 Here there is no need of an inner for loop since we have already handled it with the call of getCombinations after backtracking.

"""

class Solution:
    def getCombinations( self, idx, target, candidates, tempArray, ans ):
        
        if idx == (len(candidates)):
            if target == 0: 
                ans.append(list(tempArray))
            return
                
        if candidates[idx] <= target:
            tempArray.append(candidates[idx])
            self.getCombinations( idx, target - candidates[idx], candidates, tempArray, ans )
            tempArray.remove(candidates[idx])
            
        self.getCombinations( idx+1, target, candidates, tempArray, ans )
          
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
         
        ans = list()
        self.getCombinations( 0, target, candidates, list(), ans )
        
        return ans