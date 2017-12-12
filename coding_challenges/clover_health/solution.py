class FileConverter():
    def get_format(self, filename):
        try:
            _instructions = []
            # parse formatting file
            format_file = open(filename, "r")
            next(format_file)
            for line in format_file:
                line = line.strip('\n')
                line = line.split(",")
                _instructions.append(line)
            format_file.close()
            return _instructions
        except TypeError:
            print("Error Processing Format File")

    def get_data(self, filename):
        try:
            _data = []
            # parse data file
            data_file = open(filename, "r")
            for line in data_file:
                line = line.strip('\n')
                _data.append(line)
            data_file.close()
            return _data
        except TypeError:
            print("Error Processing Data File")
    def convert(self, datafilename, formatfilename):
        try:
            instructions = self.get_format(formatfilename)
            data = self.get_data(datafilename)
            output = []
            for d in data:
                # format
                row = {}
                for i in range(len(instructions)):
                    col_name = instructions[i][0]
                    width = int(instructions[i][1])
                    datatype = instructions[i][2]
                    # convert
                    if datatype == "integer":
                        row[col_name] = int(d[:width])
                    elif datatype == "boolean":
                        row[col_name] = bool(int(d[:width]))
                    else:
                        row[col_name] = d[:width].replace(" ", "")
                    d = d[width:]
                output.append(row)
            return output
        except TypeError:
            print("Error Processing Converting Data to Format Specification")



def parse_flatfile(datafilename, formatfilename):
    # primary variables
    format_instructions = []
    data = []

    # parse formatting file
    format_file = open(formatfilename, "r")
    next(format_file)
    for line in format_file:
        line = line.strip('\n')
        line = line.split(",")
        format_instructions.append(line)
    format_file.close()

    # parse data file
    data_file = open(datafilename, "r")
    for line in data_file:
        line = line.strip('\n')
        data.append(line)
    data_file.close()

    # convert data into output using formatting
    output = []
    for d in data:
        # format
        row = {}
        for i in range(len(format_instructions)):
            col_name = format_instructions[i][0]
            width = int(format_instructions[i][1])
            datatype = format_instructions[i][2]
            # convert
            if datatype == "integer":
                row[col_name] = int(d[:width])
            elif datatype == "boolean":
                row[col_name] = bool(int(d[:width]))
            else:
                row[col_name] = d[:width].replace(" ", "")

            d = d[width:]
        output.append(row)
    return output

#output = parse_flatfile("datafile.txt", "formatfile.txt")
f_converter = FileConverter()
print(f_converter.convert("datafile.txt", "formatfile.txt")
)
