import os
import ooziecore.lib.misc as misc
import sys
import pprint
import etc.oozie.UrlToMdn.MonthlyAggAndTopSelector.util as util

def generate_batch_with_size(params):

    fileName = params[0]
    batchSize = int(params[1])
    batchNumberWithFileSize = {}
    batchNumberWithMinMaxSize = {}
    file_map = {}
    try:
        with open(fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                filePath = line[line.find('/'):]
                file_hour_bin = os.path.dirname(os.path.dirname(filePath))
                index_1 = util.findNthIndex(file_hour_bin,'/',3)  #get the possible index of collector
                index_2 = util.findNthIndex(file_hour_bin,'/',5,True) #get the ending index of possible collector
                file_hour_bin_key_without_collector = file_hour_bin[:index_1] + file_hour_bin[index_2:]
                if (file_map.has_key(file_hour_bin_key_without_collector) == False):
                    file_map[file_hour_bin_key_without_collector] = []
                file_map[file_hour_bin_key_without_collector].append(line.strip())
        pp = pprint.PrettyPrinter(indent=4)
        ##pp.pprint(file_map)
        minMaxperHour = {}
        for key in file_map:
            dummy = []
            for l in file_map[key]:
                dummy.append(int(l.split()[4].strip()))
            minMaxperHour[key] = getMinMax(dummy)
        ##pp.pprint(minMaxperHour)
        fileName = params[2]
        temp = minMaxperHour.keys()
        temp.sort()
        with open(fileName, "w") as f:
            for k in temp:
                line =  "%s, %s, %s, %s"%(k[util.findNthIndex(k,'/',1,True) + 1:], minMaxperHour[k][0], minMaxperHour[k][1], minMaxperHour[k][2])
                f.write(line + '\n')


        dummy = []
        for k in minMaxperHour:
            dummy.append(minMaxperHour[k][2])
        pp.pprint(getMinMax(dummy))

        for key in file_map:
            listsOfPaths = file_map[key]
            list_size = len(listsOfPaths)
            i = 0
            while i < list_size:
                if batchNumberWithFileSize.has_key(key) == False:
                    batchNumberWithFileSize[key] = []
                batchNumberWithFileSize[key].append(aggregateFileSize(listsOfPaths[i : i +  batchSize]))
                i += batchSize
        ##pp.pprint(batchNumberWithFileSize)

        for key in batchNumberWithFileSize:
            batchNumberWithMinMaxSize[key] = getMinMax(batchNumberWithFileSize[key])
        ##pp.pprint(batchNumberWithMinMaxSize)
        dummy = []
        for key in batchNumberWithMinMaxSize:
            dummy.append(batchNumberWithMinMaxSize[key][2])
        ##pp.pprint(getMinMax(dummy))

        return 0
    except Exception as ex:
        import traceback
        traceback.print_exc()
        print ('Failed to get the data', ex)
        return 1
   
def getMinMax(sizeList):
    n = len(sizeList)
    if len(sizeList) % 2 == 0:
        if sizeList[0] < sizeList[1]:
            min = sizeList[0]
            max = sizeList[1]
        else:
            min = sizeList[1]
            max = sizeList[0]
        i = 2
    else:
        min = sizeList[0]
        max = sizeList[0]
        i = 1
    while i < n-1:
        if sizeList[i] > sizeList[i+1]:
            if sizeList[i] > max:
                max = sizeList[i]
            if sizeList[i+1] < min:
                min = sizeList[i+1]
        else:
            if sizeList[i+1] > max:
                max = sizeList[i+1]
            if sizeList[i] < min:
                min = sizeList[i]
        i += 2
    return [min,max,max-min]

                
            

def aggregateFileSize(pathList):
    size = 0
    for line in pathList:
        size = size +  int(line.split()[4])
    return size
           
if __name__ == '__main__':
    params = sys.argv[1:]
    if len(params) < 3:
        print ('Please provide Filename, Batch size, And Report File Name')
        sys.exit(1)
    else:
        status = generate_batch_with_size(params)
        sys.exit(status)



