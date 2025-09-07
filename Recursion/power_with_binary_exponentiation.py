class Solution:
    '''
    Brute force approach
    time complexity : O(n)
    space complexity : O(n) - Stack for recursion
    '''
    def func(self, prod, n):
        if n == 0 or prod == 1.0:
            return 1
        if n == 1:
            return prod
        return prod * self.func(prod, n-1)
    def myPow(self, x, n):
        result = self.func(x, abs(n))
        if n < 0:
            return (1/result)
        return result

    '''
    Optimal approach - using Binary exponentiation
    time complexity : O(logn)
    space complexity : O(logn) - Stack for recursion
    '''
    def myPow(self, x, n):
        def fast_pow(base, exp):
            if exp == 0:
                return 1.0

            # recursive step
            half = fast_pow(base, exp // 2)

            if exp % 2 == 0:
                # for even exponent: x^n = (x^(n/2))^2
                return half * half
            else:
                # for odd exponent: x^n = x * (x^((n-1)/2))^2
                return base * half * half

        if n < 0:
            x = 1 / x
            n = -n

        return fast_pow(x, n)