class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #creating hashmap
        h = {}
        for i,val in enumerate(nums):
            h[val]= i
        #iterating over hashmap to see if diff in map if it is return the index of it 0(1) lookup
        for x, val in enumerate(nums):
            diff = target-val;
            if(diff in h and h[diff]!=x):
                return[x,h[diff]]
        