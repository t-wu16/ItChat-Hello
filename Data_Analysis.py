import itchat 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import re 
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np 
import PIL.Image as Image 

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


def read(filename):
	try:
		return pd.read_excel(filename)
	except Exception:
		return pd.read_csv(filename)


if __name__ == '__main__':
	sns.set_palette('deep', desat=.6)
	df = read('wechat-1.xlsx')
	plt.rcParams['font.sans-serif'] = ['SimHei']

	siglist = df['Signature'].dropna()

	ser = pd.Series(map(lambda x: re.sub('<span(.*?)/span>', '', x), siglist))
	text = ''.join(ser)
	word_list = jieba.cut(text, cut_all = True)
	word_space_split = ' '.join(word_list)
	coloring = np.array(Image.open("wechat.jpg"))
	my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring, max_font_size=100, 
							random_state=42, scale=2, font_path="C:/windows/Fonts/FZSTK.TTF").generate(word_space_split)

    # 得到这个图片的色彩分布
	image_colors = ImageColorGenerator(coloring)
	plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    # 关闭横纵坐标
	plt.axis("off")
    # 显示图片
	plt.show()
