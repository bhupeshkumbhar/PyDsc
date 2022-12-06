import sys
from lib import otp

if len(sys.argv) > 3:
    inp_data = [sys.argv[1],sys.argv[2],sys.argv[3]]
    
else:
    inp_data = ["Bhupesh.Kumbhar","333K6O6QVP5SH7UR7JH7A6RGT3LZMWZB","8920392"]

otp.verify_otp(inp_data)