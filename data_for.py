data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', count, '筆資料')
print(len(data))
print(data[0])
print('-------------')
print(data[1])

sum_len = 0 
for d in data:
	sum_len = sum_len + len(d)
print('平均資料的長度為: ', sum_len / len(data))

