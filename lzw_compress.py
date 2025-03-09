def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    compressed = []
    current = ""

    print(f"{'Step':<6} {'String':<10} {'Code':<5} {'New Entry':<12} {'New Code':<5}")
    print("-" * 50)

    step = 1
    for char in data:
        new_str = current + char
        if new_str in dictionary:
            current = new_str
        else:
            compressed.append(dictionary[current])
            print(
                f"{step:<6} {current:<10} {dictionary[current]:<5} {new_str:<12} {next_code:<5}"
            )
            dictionary[new_str] = next_code
            next_code += 1
            current = char
        step += 1

    if current:
        compressed.append(dictionary[current])
        print(f"{step:<6} {current:<10} {dictionary[current]:<5} {'-':<12} {'-':<5}")

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
