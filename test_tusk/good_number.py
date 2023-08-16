def get_good_num(s):
	lst = []
	for i in range(len(s)-2):
		if s[i].isdigit() and (s[i] == s[i+1] == s[i+2]):
			lst.append(int(s[i]*3))
	return max(lst) if lst else 'Такого числа нет'
		

print(get_good_num('aa333as777dq555weasf666'))
