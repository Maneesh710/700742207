it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.add('Tesla')
it_companies.add('Bugatti')
it_companies.add('Volvo')
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Microsoft')
print(it_companies)

#Join A and B
print(A.union(B))

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
print(A.union(B))
print(B.union(A))

#What is the symmetric difference between A and B
print(A.difference(B))

#Delete the sets completely
A.clear()
print(A)
B.clear()
print(B)

#Convert the ages to a set and compare the length of the list and the set.
print(set(age))
