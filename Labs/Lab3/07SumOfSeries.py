# sum of series 1 – 2 + 3 – 4 + 5 – 6 + 7 ... n
n = int(input("Enter a number "))
ans = 0
for i in range(1,n+1):
	if(i%2==0):
		ans-=i
	else:
		ans+=i
print(ans)
