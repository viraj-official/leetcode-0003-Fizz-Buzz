class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        return result
solution = Solution()

# Call the fizzBuzz method and pass the value of n
n = 15
result = solution.fizzBuzz(n)

# Print the result
print(result)
