import binascii

# Function to calculate CRC32 checksum
def calculate_crc32(data):
    crc_accumulator = 0xffffffff
    for byte in data:
        crc_accumulator ^= byte
        for _ in range(8):
            if crc_accumulator & 1:
                crc_accumulator = (crc_accumulator >> 1) ^ 0xedb88320
            else:
                crc_accumulator >>= 1
    return crc_accumulator ^ 0xffffffff

# Raw hex data from memory
memory_hex="f3e1cfed23cd6b6457adf950e1b199f2e4b6a9c64c618032022b7793433a2cab6a930d2ad414fa1b2f6f5d256bf647c4f56cd95a12ad64e9"

# Convert hex string to bytes
memory_bytes = binascii.unhexlify(memory_hex)

# Extract pairs of checksums (each checksum is 4 bytes)
checksums = [memory_bytes[i:i+4] for i in range(0, len(memory_bytes), 4)]

# Brute-force each pair of checksums to find corresponding symbols
flag = ""
for checksum in checksums:
    found = False
    for i in range(256):
        for j in range(256):
            data = bytes([i, j])
            if calculate_crc32(data) == int.from_bytes(checksum, byteorder='little'):
                flag += chr(i) + chr(j)
                found = True
                break
        if found:
            break

print("Flag:", flag)
