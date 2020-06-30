import pickle  # ('object' or text) Serialize or Deserialize. Text file can be "binary" by using this.

# File name and data.
bfilename = 'test.bin'
tfilename = 'test.txt'

data1 = 77
data2 = "Hello, world!"
data3 = ["car", "apple", "house"]

# Write binary file
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f)  # dumps() -> 'text' serialization. # dump() -> Write into a file.
    pickle.dump(data2, f)
    pickle.dump(data3, f)

# Write text file
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))

# Binary files can not be read by people.
# But, we can read it by Python.

# Read binary file
with open(bfilename, 'rb') as f:
    b = pickle.load(f)  # loads() -> 'text' deserialization # load() -> Read binary file.
    print(type(b), ' Binary Read1 | ', b)
    b = pickle.load(f)
    print(type(b), ' Binary Read2 | ', b)
    b = pickle.load(f)
    print(type(b), ' Binary Read3 | ', b)

# Read text file
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), 'Text Read' + str(i) + ' | ', line, end='')
