import urllib2,re
def laysource(url, data, cookie, referer):
	headers = {'Cookie':cookie,'Referer':referer}
	req = urllib2.Request(url , data, headers)
	opreq = urllib2.urlopen(req).read()
	if len(data) == 0:
		l1 = opreq.index('<table>')
		l2 = opreq.index('</table>')
		sour = opreq[l1:l2]
		return re.findall('<li>(.*?)</li>',sour, re.DOTALL)
	else:
		return opreq
def xuly(unscrambled,wordlist):
	ch = []
	for items in unscrambled:
		for char in wordlist.split():
			if sorted(list(items)) == sorted(list(char)):
				ch.append(char)
	return ','.join(ch)
def ketqua(url,data,cookie,referer):
	dota = "solution=%s&submitbutton=submit++++++++++++%%28remaining+time%%3A+25+seconds%%29"%data
	if 'wrong' in laysource(url,data,cookie,referer):
		print 'Sai roai!'
	else:
		print 'Thanh cong!'

if __name__ == '__main__':
	url = r'https://www.hackthissite.org/missions/prog/1/index.php'
	cookie = r'__utma=198402870.1510861788.1478252350.1478362271.1478400979.5; __utmz=198402870.1478252350.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=e7pagvk74608dcjd8v7qamefp5; __utmc=198402870'
	referer = r'https://www.hackthissite.org/missions/prog/1/index.php'
	unscrambled = laysource(url,'',cookie,referer)
	wordlist = open('wordlist.txt','r').read()
	data = xuly(unscrambled,wordlist)
	ketqua(url,data,cookie,referer)
