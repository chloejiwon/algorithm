class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        result = []
        
        for idx, val in enumerate(expression):
            if val in "-+*":
                a = self.diffWaysToCompute(expression[:idx])
                b = self.diffWaysToCompute(expression[idx+1:])
                result.extend(compute(a,b,val))
                
        
        return result
