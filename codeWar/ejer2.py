def bool_to_word(boolean):
   return 'No' if boolean == False else 'Yes'

print(bool_to_word(False))

def divisible_by(numbers, divisor):
   divisors = []
   if len(numbers) <= 0:
      return [0,1,2,3,4,5,6,7,8,9,10]
   for num in numbers:
      if num % divisor == 0:
         divisors.append(num)   
   return divisors

print(divisible_by([1,2,3,4,5,6],2))