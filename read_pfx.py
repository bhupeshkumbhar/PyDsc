from digital_certificate.cert import Certificate

# Instantiate the class with the file path or the binary file content 
cert = Certificate(
    pfx_file="dsc_1100.pfx",
    password=b"Test@123"
)

# Read PFX file
cert.read_pfx_file()

# Get Serial Number
print(cert.serial_number())

# Get not valid before date
print(cert.not_valid_before())

# Get not valid after date
print(cert.not_valid_after())

# Get subject name
print(cert.subject())

# Get owner name
print(cert.common_name())

# Get Issuer name
print(cert.issuer())