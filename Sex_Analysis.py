import itchat 
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif'] = ['SimHei']	# 步骤一 （替换sans-serif字体）
itchat.auto_login(hotReload=True)	# 登录后

# 第一个是自己，不需要，从第二个开始获取
friendList = itchat.get_friends(update=True)[1:]

# 0表示未知，1表示男性，2表示女性
sexDict = {}

total = len(friendList)
print('好友总数为:',total)

for friend in friendList:
	if not friend['Sex'] in sexDict:
		sexDict[friend['Sex']] = 0
	sexDict[friend['Sex']] += 1
unknown = sexDict[0]
male = sexDict[1]
female = sexDict[2]

'''matplotlib绘制饼状图pie'''
# 调节图形宽、高
plt.figure(figsize = (5, 5))
# 颜色
colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
# 标签
labels = ['未知', '男性', '女性']
# 将某部分分割出来，间隙为0.1
explode = (0, 0.1, 0)
# autopct, 圆里面的文本格式, %3.1f%%表示小数有3位，整数有一位的浮点数
plt.pie([unknown, male, female], labels = labels, explode = explode, colors = colors, autopct = '%1.1f%%', shadow = True)
plt.legend()
plt.show()