def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    compressed = []
    current = ""

    for char in data:
        new_str = current + char
        if new_str in dictionary:
            current = new_str
        else:
            compressed.append(dictionary[current])
            dictionary[new_str] = next_code
            next_code += 1
            current = char

    if current:
        compressed.append(dictionary[current])

    return compressed


def lzw_decompress(compressed):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    current = chr(compressed[0])
    decompressed = [current]

    for code in compressed[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current + current[0]
        else:
            raise ValueError("Kode tidak valid dalam dekompresi LZW.")

        decompressed.append(entry)
        dictionary[next_code] = current + entry[0]
        next_code += 1
        current = entry

    return "".join(decompressed)


text = input("Masukan Teks Anda: ")
compressed_data = lzw_compress(text)
print("Kompresi:", compressed_data)

decompressed_text = lzw_decompress(compressed_data)
print("Dekompresi:", decompressed_text)
