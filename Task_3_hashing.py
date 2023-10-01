def read_input(Input_file):
	with open(Input_file, "r") as f:
		content = f.readlines()
	content = [x.strip() for x in content]
			
	return content
	
def main():
	read = read_input("input.txt")
	n = int(read[0])
	records = read[1:]
	a = []
	ans,u,v = 0,-1,-1
	for i in range(0, n):
		t = [int(x) for x in records[i].split()]
		t.sort()
		if ans < t[0]:
			ans = t[0]
			u = v = i
		t.append(i)
		a.append(t)

	from operator import itemgetter
	a.sort(key=itemgetter(1,2,0),reverse=True)
	i = 0
	while i+1 < n:
		if(a[i][1]==a[i+1][1] and a[i][2]==a[i+1][2]):
			t = min(a[i][0]+a[i+1][0],a[i][1])
			if ans < t:
				ans = t
				u = a[i][3]
				v = a[i+1][3]
		i += 1
		while (i==0 or (a[i][1]==a[i-1][1] and a[i][2]==a[i-1][2]) ) and i+1<len(a):
			i += 1
		
	if u == v:
		with open("output.txt", "w") as f:
			f.write("1\n")
			f.write(str(u + 1) + '\n') 
			f.write(str(ans))
	else:
		with open("output.txt", "w") as f:
			f.write("2\n")
			f.write(str(u + 1) + " ")
			f.write(str(v + 1))
			f.write('\n')
			f.write(str(ans))
			
if __name__ == "__main__":
	main()		
			