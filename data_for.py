data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', count, '筆資料')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1

		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))
print(wc['a'])

while True:
	word = input('你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現的次數為', wc[word])
	else:
		print('這個字不存在')
print('感謝您使用本查詢')










# print(len(data))
# print(data[0])
# print('-------------')
# print(data[1])

# sum_len = 0 
# for d in data:
# 	sum_len = sum_len + len(d)
# print('平均資料的長度為: ', sum_len / len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆資料長度小於100')

	
