# 18. Sort dictionary by values
# Approach: Use sorted with lambda.

d = {'a': 3, 'b': 1, 'c': 2}
print(dict(sorted(d.items(), key=lambda x: x[1])))