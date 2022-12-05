import os

def delete(inp_file):
    files = {"_img","_out"}
    for file in files:
        file_name = inp_file.replace("_inp",file)
        file_name = os.path.abspath(file_name)
        os.remove(file_name)