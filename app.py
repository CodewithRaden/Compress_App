from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# LZW Compression Function
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


# LZW Decompression Function
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
            return "Error: Invalid compressed data."

        decompressed.append(entry)
        dictionary[next_code] = current + entry[0]
        next_code += 1
        current = entry

    return "".join(decompressed)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_text():
    data = request.json
    text = data.get("text", "")
    mode = data.get("mode", "encode")

    if mode == "encode":
        compressed = lzw_compress(text)
        output = " ".join(map(str, compressed))
    else:
        try:
            compressed_data = list(map(int, text.split()))
            output = lzw_decompress(compressed_data)
        except ValueError:
            output = "Error: Invalid input for decompression."

    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(debug=True)
