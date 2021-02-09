import binascii

tmp = (
    "47494638396101000100800000000000ffffff21f9"
    + "0401000000002c000000000100010000020144003b"
)

gif = binascii.unhexlify(tmp)
print(gif)
