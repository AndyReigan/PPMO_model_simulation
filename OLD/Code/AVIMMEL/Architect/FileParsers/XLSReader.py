import xlrd


class XlSReader:
    def __init__(self):
        self.dictnameSheets = {}
        self.rb = None
        self.readtype = None
        self.firstRow = None
        self.lastRow = None
        self.currentRow = None

    def openFile(self, fileName):
        self.rb = xlrd.open_workbook(fileName, formatting_info=True)
        self.dictnameSheets = {}
        self._readNames()
        self.currentRow = self.firstRow

    def _readNames(self):
        for sheetNum in range(self.rb.nsheets):
            nameList = []
            sheet = self.rb.sheet_by_index(sheetNum)
            for colnum in range(sheet.ncols):
                nameList.append(sheet.cell(0, colnum).value)
            self.dictnameSheets[sheetNum] = nameList

    def setReadProperties(self, index=None):
        indexType = type(index)
        if indexType == type(None):
            self.readtype = "auto"
            self.firstRow = 1
            self.lastRow = self.rb.sheet_by_index[0].nrows
        elif indexType == type(int()):
            self.readtype = "local"
            self.firstRow = index
            self.lastRow = index
        else:
            self.readtype = "range"
            self.firstRow = index[0]
            self.lastRow = index[1]

    def breakConditions(self):
        return self.currentRow > self.lastRow

    def getValue(self, valData):
        outData = {}
        for data in valData:
            sheet = self.rb.sheet_by_index(data[0])
            colnum = self.dictnameSheets[data[0]].index(data[1])
            if sheet.cell(self.currentRow, colnum).value == 'NO VAL':
                outData[data[1]] = None
            else:
                outData[data[1]] = float(sheet.cell(self.currentRow, colnum).value)
        self.currentRow += 1
        return outData
