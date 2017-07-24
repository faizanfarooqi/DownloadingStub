'''
This script exports urls af decore objects in a file. Urls are formed by concatinating bucketUrl with max
archive name which are taken from json file. First argument ti the script is input json file and 2nd argument 
is output file to export links.
Usage: exportAssetsUrlsFromAppJson.py -i <input json> -o <output file>
created by Faizan-ur-Rehman. Last Updated 24 July, 2017
'''
import os
import sys
import json
import getopt
from pprint import pprint

def main(argv): 
	dwRetVal = 0 #denotes success
	strJsonFileLocation = None
	strOutputFileLocation = None
	boolHelpRequired = False
	listOptions, listArguments = getopt.getopt(argv, "hi:o:t:", ["help", "inputFile=", "outputFile=", "assetType="])
	#parse command line arguments...
	try:
		for listOption, strArgument in listOptions:
			if listOption in ("-h", "--help"):
                                try:
                                        fstreamHelpFile = open('help_exportAssetUrlFromJson.txt', 'r')  
                                except IOError:
                                        print 'Usage:\n\texportAssetUrlFromJson.py - i <input file path> -o <output file path> -t <unity|max>'
                                if fstreamHelpFile is not None:
                                        print fstreamHelpFile.read()
                                
				#print 'Usage:\n\texportAssetUrlFromJson.py - i <input file path> -o <output file path> -t <unity|max>'
				boolHelpRequired = True
			elif listOption in ("-i", "--inputFile"):
				strJsonFileLocation = strArgument
			elif listOption in ("-o", "--outputFile"):
				strOutputFileLocation = strArgument
	except getopt.GetoptError as strError: 
		print 'ERROR: ', strError 
		print 'Usage:\n\texportAssetUrlFromJson.py - i <input file path> -o <output file path> -t <unity|max>'
		dwRetVal = -8
        if boolHelpRequired is False:
			if strJsonFileLocation is not None and strOutputFileLocation is not None:
				print(sys.argv)
				if os.path.exists(strJsonFileLocation): 
					fstreamInputDataFile = None
					try:
						fstreamInputDataFile = open(strJsonFileLocation, 'r')    
					except IOError:
						print("File " + strJsonFileLocation + " could not be opened.")
					if fstreamInputDataFile is not None:
						objData = json.load(fstreamInputDataFile)
						print ("Json loaded from the file is : ")
						pprint(objData)
						fstreamTargetOutputFile = None
						try:
							fstreamTargetOutputFile = open(strOutputFileLocation, 'w')
						except:
							print("File " + strOutputFileLocation + " could not be opened.")
						if fstreamTargetOutputFile is not None:
							'''
							strFileName = objData[strKeyPassed]["fileName"]
							print("Filename from json file with extension is " + strFileName)
							strBucketUrl = objData[strKeyPassed]["bucketUrl"]
							print("Bucket URL formed taken from json file is " + strBucketUrl)
							strAssetUrl =  strBucketUrl + '/' + strFileName        #asset url generated
							print ("Asset Url generated is " + strAssetUrl)
							'''
							strAssetBaseUrl = objData['MaxFileBaseURL']
							for objAsset in objData['DecoreObjects']:
									strAssetUrl = strAssetBaseUrl + objAsset['MaxArchive']
									print("Url needs to be downloaded is " + strAssetUrl)
									fstreamTargetOutputFile.write(strAssetUrl+"\n")
							fstreamTargetOutputFile.close()
						else:
								dwRetVal = -7
								print "ERROR: Output file could not be opened"
					else:
							dwRetVal = -4
							print "ERROR: Input json could not be opened"                                   
						
				else:
						dwRetVal = -3
						print "ERROR: Input json file does not exists."
			else:
					dwRetVal = -1
					print "ERROR: You must provide two arguments. First Json file path and second output file path to out value of keys exported from json file."
	return dwRetVal
	
if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
