import sys
from lib import auth

if len(sys.argv) > 1:
    inp_data = sys.argv[1]
else:
    inp_data = 'Bhupesh.Kumbhar,333K6O6QVP5SH7UR7JH7A6RGT3LZMWZB,8920392'

inp_data = inp_data.split(",")
auth.auth_user(inp_data)