import os

def del_xfile(inp_data):
    inp_path = inp_data[0]
    files = {"_img","_out"}
    for file in files:
        file_path = inp_path.replace("_inp",file)
        file_path = os.path.abspath(file_path)
        os.remove(file_path)