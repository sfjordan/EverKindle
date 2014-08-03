import sys
import urllib2

#get arguments
if (len(sys.argv)>2):
	print("Usage: EverKindle [your_notes_directory]")
	print("        [if running from within directory, leave blank]")
	sys.exit(0)
elif (len(sys.argv) == 2):
	path = sys.argv[1]
else:
	path = ''

try:
	index = open(path+'/index.html','r')
except Exception,e:
	print 'IOError reading index.html!'
	print str(e)

fullstr = index.read()
index.close()

numNotes = len(fullstr.split('href'))

urls = []
fullstrs = []

for n in range(1, numNotes):
	urls.append(urllib2.unquote(fullstr.split('href')[n].split('"')[1]))

for n in range(0,len(urls)):
	urls[n] = urls[n].replace('&amp;','&')

print 'reading notes files...'

for url in urls:
	f = open(path+url, 'r')
	fullstrs.append(f.read())

#find the titles and make them pretty:
for n in range(0, len(fullstrs)):
	fullstrs[n] = fullstrs[n].replace('<title>','<table border="0" style="background-color: #D4DDE5" width="100%"><tbody><tr><td><h1>')
	fullstrs[n] = fullstrs[n].replace('</title>','</h1><br/></td></tr></tbody></table>')


#flip it!
fullstrs.reverse()

#write it!
print 'writing notes to FULL_NOTES_FILE.html...',
newf = open(path+'/FULL_NOTES_FILE.html','w')
for note in fullstrs:
	newf.write('<html>')
	newf.write(note)
	newf.write('</html>')

newf.close()

print 'done.'

