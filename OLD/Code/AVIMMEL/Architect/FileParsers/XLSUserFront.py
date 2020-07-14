from Code.AVIMMEL.Architect.FileParsers.XLSReader import XlSReader


class XLSUserFront:
    def loadData(self, fileName, data, index=None):
        xlsb = XlSReader()
        xlsb.openFile(fileName)
        xlsb.setReadProperties(index)
        outdict = {}
        for singledata in data:
            outdict[singledata[1]] = []
        while not xlsb.breakConditions():
            rowData = (xlsb.getValue(data))
            for singledata in data:
                outdict[singledata[1]].append(rowData[singledata[1]])
        xlsb.rb.release_resources()
        return outdict