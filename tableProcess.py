# where we can singularly process the table


import pickle, os
from bs4 import BeautifulSoup as bs
import helpers as h


# consider the case where there are multiple rank columns
# you might have to resort based off the data in that particular column

def singleTableProcess(file):

	# unpickle the raw table, [sort_list, soup]
	sort_list, tables = h._depickle(file)


	rows = tables[0]('tbody')[0]('tr')

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

	# clist.sort()
	# clist = list(filter(None, clist))
	fdir = 'pdatasets/'+file[:-12]
	h._pickle(clist, fdir)
    return clist

def processDir(dir):
	# signle table
    return
