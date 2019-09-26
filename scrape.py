from bs4 import BeautifulSoup as bs
import requests, sys, time, pickle
from urllib.request import urlopen

sys.setrecursionlimit(500000)
# solely to download and save tables from wiki in python-usable format
# should handle multiple rank columns

def dec(obj):
	if isinstance(obj, list):
		obj[:] = [r - 1 for r in obj]
	else:
		obj -= 1
	return obj

def _pickle(data, file):
	of = open(file, 'wb')
	pickle.dump(data, of)
	of.close

def _depickle(file):
	infile = open(file, 'rb')
	return pickle.load(infile)


# a catalog of what data we want from the desired wiki table
class tableLogger:
	def __init__(self, label_col, rank_col, row_offset, table_offset=1):
		self.label_col = dec(label_col)
		self.rank_col = dec(rank_col)
		self.row_offset = dec(row_offset)
		self.table_offset = dec(table_offset)

# gather just necessary columns from table
def singleTableProcess(table, tablog):
	# TODO:
	# - tuple structure [country_id, rank]?
	# - add more statistics, like weighted ratios
	# - add iteration for multiple ranking columns

	rows = table('tbody')[0]('tr')

	numrows = len(rows)

	clist = []
	# cdict = {}

	# REM: these are *technically* unsorted, which is useful for multiple rankings
	for n in range(tablog.row_offset, numrows):
		try:
			cname = rows[n]('td')[tablog.label_col]('a')[0].text
			crank = rows[n]('td')[tablog.rank_col].text.strip().replace(',' , '')
		except IndexError:
			break
		if not (cname and crank):
			continue
		# print(cname, crank)
		clist.append([cname, float(crank)])

	return clist



def reqandsavehtml(url):
	req = requests.get(url)
	soup = bs(req.content, 'html.parser')
	tableTitle = soup.find(id="firstHeading").text
	tables = soup('table', {'class':'wikitable'})
	fname = tableTitle[21:] + " page.html"
	fpath = 'html/' + fname
	pickle(req, fpath)
	return fpath

def openandsoupifyhtml(file):
	req = _depickle(file)
	soup = bs(req.content, 'html.parser')
	return soup

# TODO:
# this is the only time we need world 'accurate' columns?

def scrape(url, tablog):
	try:
		req = requests.get(url)
	except requests.exceptions.RequestException as e:
		print(e + 'for url ' + url)
		break

	soup = bs(req.content, 'html.parser')
	tableTitle = soup.find(id="firstHeading").text
	tables = soup('table', {'class':'wikitable'})
	table = tables[tablog.table_offset]

	print("saving tables from page " + tableTitle + "...")

	fname = tableTitle[21:] + " data"
	fpath = 'pdatasets/' + fname


	clist = singleTableProcess(table, tablog)
	saveData = (clist, tablog)
	sys.setrecursionlimit(50000)
	_pickle(saveData, fpath)
	return clist, fpath

def scrapeURLFile(file):
	print('Starting scrape of "'+file+'"')
	infile = open(file, 'rb')
	while True:
		url = infile.readline().decode().strip()
		nums = infile.readline().decode().split()
		if not (url and nums): break #EOF
		nums = [int(x) for x in nums]
		tablog = tableLogger(*nums)
		scrape(url, tablog)
		time.sleep(1)
	return


def testHTML(file, tablog):
	soup = openandsoupifyhtml(file)
	tableTitle = soup.find(id="firstHeading").text
	tables = soup('table', {'class':'wikitable'})
	table = tables[0]

	c = singleTableProcess(table, tablog)
	return c


# tablog = tableLogger(1, 4, 3)
# clist, fnmae = scrape(url, tablog)
# print(fnmae)
# c = singleTableProcess(file)
# c = scrape(url, 1, 4, 1)

n = scrapeURLFile('single.txt')

# tablog = tableLogger(1, 11, 1)
#
# # file = reqandsavehtml(url)
#
# file = 'html/household debt page.html'
# c = testHTML(file, tablog)


# q = _depickle('pdatasets/male to female income ratio tables')

# print(n)
