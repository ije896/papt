from bs4 import BeautifulSoup as bs
import requests, pickle


def _pickle(data, file):
	of = open(file, 'wb')
	pickle.dump(data, of)
	of.close

def _depickle(file):
	infile = open(file, 'rb')
	return pickle.load(infile)

# solely to download the table from a website
def scrape(url, label_col, rank_col, col_offset=2):
	label_col -= 1
	rank_col -= 1
	# col_offset = 2
	
	# fname = 'datasets/un_population' #should be label derived from website
	# req = _depickle(fname)

	req = requests.get(url)
	#throw in error handling for request

	soup = bs(req.content, 'html.parser')

	label = soup.find(id="firstHeading").text
	fdir = 'datasets/'+label

	print(label)

	table = soup('table', {'class':'wikitable'})

	rows = table[0]('tbody')[0]('tr')

	numrows = len(rows)

	print(numrows)

	# ('tr')[n+1'th country]('td')[1]('a')[0].text
	# cname = soup('table', {'class':'wikitable'})[0]('tr')[2]('td')[1]('a')[0].text
	clist = []
	# cdict = {}
	#uple structure [country_id, rank] #add more statistics, like weighted ratios
	for n in range(col_offset, numrows):
		cname = rows[n]('td')[label_col]('a')[0].text
		crank = rows[n]('td')[rank_col].text.strip().replace(',' , '')
		clist.append([cname, float(crank)])
		# 

	# clist.sort()
	# clist = list(filter(None, clist))
	_pickle(clist, fdir)

	return clist


url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
# url = 'https://en.wikipedia.org/wiki/List_of_countries_by_male_to_female_income_ratio'

# gather country names:
c = scrape(url, 2, 6, 2)
# c = scrape(url, 1, 4, 1)


# a = _depickle('datasets/listofcountries')

# cdict = {}

# for n in range(0, len(a)):
# 	cdict[a[n].lower()] = n


# print(soup.findAll('a'))




