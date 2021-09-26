def smallerNumbersThanCurrent( nums):
    d = {}
    for index, value in enumerate(sorted(nums)):
        if value not in d:
            d[value] = index

    # iterate through the nums and fetch its corresponding hash table value
    ans = [d[value] for value in nums]
    return ans
ans=smallerNumbersThanCurrent([4,1,2,3,7,2])
print(ans)


#method 2:0(n2)
a=[4,1,2,3,7,2]
lst=[]
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]>a[j] and i!=j:
            count=count+1
    lst.append(count)
print(lst)