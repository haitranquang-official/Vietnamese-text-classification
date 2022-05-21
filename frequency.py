strArr = ["mot", "hai", "hai", "ba", "ba", "ba"]

elements_count = {}

# iterating over the elements for frequency
for element in strArr:
   if element in elements_count:
      elements_count[element] += 1
   else:
      elements_count[element] = 1

# printing the elements frequencies
for key, value in elements_count.items():
   print(f"{key}: {value}")