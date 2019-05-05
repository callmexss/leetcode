class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        fizz, buzz = 0, 0
        
        for i in range(1, n + 1):
            fizz += 1
            buzz += 1
            
            if fizz == 3 and buzz == 5:
                ret.append("FizzBuzz")
                fizz, buzz = 0, 0
                
            elif fizz == 3:
                ret.append("Fizz")
                fizz = 0
                
            elif buzz == 5:
                ret.append("Buzz")
                buzz = 0
                
            else:
                ret.append(str(i))
                
        return ret
        
