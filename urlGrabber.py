import urllib2

baseURL = "http://library.marist.edu/archives/LTP/" # home page archive
startURL = "http://library.marist.edu/archives/LTP/LTP.xml" # seed url 


def pagecrawl(url, space1, space2, section):
	response = urllib2.urlopen(url) #opens the url
	page_source= response.read() # stores the html of the url
	
	while page_source[space2:].find('xlink:href=')!=-1: #loops through each link on the page
		space1 = page_source.find('xlink:href=', space2 ) + len('xlink:href=') +1
		space2 = page_source.find('>', space1)
		endURL = page_source[space1:space2-1] # grabs the subSeries
		if '.xml' in endURL: #only grabs pages in the archive, .xml
			if " " in endURL: 
				endURL = endURL.replace(" ", "%20") #replaces spaces with %20
			if section != "":
				childURL = baseURL + section +"/" +endURL # adds subSeries with section if it has a section
			else:
				childURL = baseURL +endURL # url is just a series, so it has no section
				sectionsURL.append(childURL)
			listURL.append(childURL)
			

sectionsURL =[]  #list of all the series urls
listURL = []	#complete list of urls, including all the series subseries

pagecrawl(startURL, 0, 0, "") # starts the page crawl with the start url, starting spaces being the beginning of the document. originally only gets the series urls.

for sectionURL in sectionsURL:
	pagecrawl(sectionURL, 0, 0,sectionURL.split('/')[len(sectionURL.split()) -3]) # this loop gets each subseries in a series

with open("Output.txt", "w") as text_file: # writes out the urls to output.txt 
    for item in listURL:
    	text_file.write(str.format("%s\n" % item))

