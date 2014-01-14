import urllib2
'''
with open("pagesource.txt", "w") as text_file:
    text_file.write(str.format(page_source))

'''
baseURL = "http://library.marist.edu/archives/LTP/" # home page archive

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
				childURL = baseURL +endURL
				sectionsURL.append(childURL)
			listURL.append(childURL)
			
startURL = "http://library.marist.edu/archives/LTP/LTP.xml"

sectionsURL =[] 
listURL = []
listLen =0

pagecrawl(startURL, 0, 0, "")

for sectionURL in sectionsURL:
	
	pagecrawl(sectionURL, 0, 0,sectionURL.split('/')[len(sectionURL.split()) -3])


with open("Output.txt", "w") as text_file:
    for item in listURL:
    	text_file.write(str.format("%s\n" % item))

