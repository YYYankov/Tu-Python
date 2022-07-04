
binary_file = open("document.bin", "rb")
text="This is good"
encoded=text.encode("utf-8")
binary_file.seek(0)
binary_data=binary_file.read(4)
print("binary:",binary_data)
text=binary_data.decode("utf-8")
print("Decoded data:",text)
binary_file.close()
