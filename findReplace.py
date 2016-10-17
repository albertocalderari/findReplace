__author__ = 'alberto'
__version__ = '0.1'


# findReplace function
def findReplace(fileToProcess, toFind, toReplace, newFile=None, folder='', overWrite=False):
    # open the file
    cursor = open(folder+'/'+fileToProcess, 'r')
    # define the output string
    newLine = ''
    # loop through the lines and replace the string
    newLine += [line.replace(toFind, toReplace) for line in cursor]
    cursor.close()
    # overwrite the file
    if overWrite:
        cursor = open(folder+'/'+fileToProcess, 'w')
        cursor.write(newLine)
    else:
        cursor = open(folder+'/'+newFile, 'w')
        cursor.write(newLine)

