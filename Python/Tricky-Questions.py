# Dictionary Comprehension
count = { n : 0 for n in nums }
count = dict((n, 0) for n in nums)

# Not Dictionary Comprehension
count = { (n, 0) for n in nums }  # Creates a set of tuple pairs
