import itchat 
import pandas as pd

def login_and_getData(columns=[]):
	itchat.auto_login(hotReload=True)
	friendList = itchat.get_friends(update=True)[1:]

	if len(columns) == 0:
		columns = friendList[0].keys()
	# print(columns,"\n")

	df = pd.DataFrame(columns=columns)	# 列名是好友属性
	val = [0] * len(friendList)
	# print(val,'\n')

# df一行存储所有好友的某一个属性
	for c in columns:
		for i in range(len(friendList)):
			val[i] = friendList[i][c]
		df[c] = val
	return df

df = login_and_getData()
df.to_excel('wechat-1.xlsx')