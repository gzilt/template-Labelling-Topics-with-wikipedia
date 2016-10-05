import wikipedia
import pandas

def get_wikiPages(filename):
	pagesFile = open(filename,"r")
	df = pandas.DataFrame(columns=['title','content'])
	titles = list()
	content = list()
	for pageName in pagesFile:
		try:
			page = wikipedia.page(pageName)
			titles.append(page.title)
			content.append(page.content)
		except:
			continue
	df['title'] = titles
	df['content'] = content	
	return df

df = get_wikiPages('test_categories.txt')		
print(df)

df.to_csv('test_cat.csv','a',header=True, cols=["title","content"],encoding='utf-8')
# import codecs

# with codecs.open("testCategory.csv", "a", encoding='utf-8') as file:
# 	file.writelines(df['title'])




