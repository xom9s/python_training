import struct

# Define an integer value
number = 0x12345678

# Convert the integer to bytes in little-endian format
little_endian_bytes = struct.pack('<I', number)
print("Little-endian:", little_endian_bytes)

# Convert the integer to bytes in big-endian format
big_endian_bytes = struct.pack('>I', number)
print("Big-endian:", big_endian_bytes)

# Unpack the bytes back to integers to verify
little_endian_number = struct.unpack('<I', little_endian_bytes)[0]
big_endian_number = struct.unpack('>I', big_endian_bytes)[0]
print("Little-endian number:", little_endian_number)
print("Big-endian number:", big_endian_number)
