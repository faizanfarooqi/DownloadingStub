# script to export filname under key thumbnail or assetBundle from json file(taken as argument) to output file(taken as second argument)
# and type (unity or max) as third agrument
# created by Faizan-ur-Rehman Last Updated 17 July, 2017
import os
import sys
import json
import getopt
import zipfile
from pprint import pprint

def getFileNameFromUrl(a_strUrl):
    listStrTokens = a_strUrl.split("/")
    return (listStrTokens[len(listStrTokens)-1])

def getFileNameFromUrlWithoutExtension(a_strUrl):
    listStrTokens = a_strUrl.split("/")
    return (listStrTokens[len(listStrTokens)-1]).split('.')[0]

def main(argv): 
	dwRetVal = 0 #denotes success
	strLinksFileLocation = None
	strDownloadDirectory = None
	boolHelpRequired = False
	listOptions, listArguments = getopt.getopt(argv, "hi:o:t:", ["help", "linksFile=", "outputDirectory=", "type="])
	#parse command line arguments...
	try:
		for strOption, strArgument in listOptions:
			if strOption in ("-h", "--help"):
                                fstreamHelpFile = None
                                try:
                                        fstreamHelpFile = open('help_downlaodAssets.txt', 'r')    
                                except IOError:
                                        print 'Usage:\n\tdownloadAssets.py - i <input file path> -o <output file path> -t <unity|max>'
                                if fstreamHelpFile is not None:
                                        print fstreamHelpFile.read()
                                
				#print 'Usage:\n\tdownlaodAssets.py - i <input file path> -o <output file path> -t <unity|max>'
                                boolHelpRequired = True
			elif strOption in ("-i", "--linksFile"):
				strLinksFileLocation = strArgument
			elif strOption in ("-o", "--outputDirectory"):
				strDownloadDirectory = strArgument
	except getopt.GetoptError as strError: 
		print 'ERROR: ', strError 
		print 'Usage:\n\texportAssetFileName.py - i <input file path> -o <output file path> -t <unity|max>'
		dwRetVal = -8

        if boolHelpRequired is False:
                print(argv)
                if strLinksFileLocation is not None and strDownloadDirectory is not None:
                        if os.path.exists(strLinksFileLocation):
                                if os.path.exists(strDownloadDirectory):
                                        with open("C:\Scripts\download file\links.dat") as f:
                                            for line in f:
                                                line = line.replace("\n","")
                                                print ("Link to be downloaded is " + line)
                                                print ("python -m wget -o " + "\"" + strDownloadDirectory + "\"" + " " + line)
                                                os.system("python -m wget -o " + "\"" + strDownloadDirectory + "\"" + " " + line)
                                                strAssetZipPath = strDownloadDirectory+"\\"+getFileNameFromUrl(line)
                                                print strAssetZipPath
                                                objZipFile = zipfile.ZipFile(strAssetZipPath)
                                                strZipExtractionPath = strDownloadDirectory+"\\"+getFileNameFromUrlWithoutExtension(line)+"\\"
                                                print strZipExtractionPath
                                                objZipFile.extractall(strZipExtractionPath)
                                                objZipFile.close()
                                                #print ("7z x \""+strDownloadDirectory+"\\"+getFileNameFromUrl(line)+ "\" -o"+ "\"" + strDownloadDirectory + "\\"+getFileNameFromUrlWithoutExtension(line)+"\"")
                                                #os.system ("7z x \""+strDownloadDirectory+"\\"+getFileNameFromUrl(line)+ "\" -o"+ "\"" + strDownloadDirectory + "\\"+getFileNameFromUrlWithoutExtension(line)+"\"")
                                        #url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
                                        #print ("python -m wget http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3")
                                        #os.system("python -m wget http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3")
                                        #os.system("del *.zip")
                                else:
                                        dwRetVal = -3
                                        print "ERROR: Download directory could not be found."
                        else:
                                dwRetVal = -2
                                print "ERROR: Input links file location could not be found."          
                else:
                        dwRetVal = -1
                        print "ERROR: You must provide two arguments. First download links file path and second output directory to download files in it."
	return dwRetVal
	
if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
