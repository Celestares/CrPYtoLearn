from flask import Flask, render_template, request
from CryptoPackage import shift_cipher, monoalpha_cipher, railfence_cipher, column_cipher, vernam_cipher, aes, dhkey_exchange

app = Flask(__name__)


@app.route("/")  # Homepage
def home():
    return render_template("home.html")


#
#
#
#


@app.route("/learn")  # Learn various security topics
def learn():
    return render_template("learn/learn.html", title="Learning Materials")


@app.route("/learn/need_security")
def learn_security():
    return render_template("learn/learn_security.html", title="Learn - Need for security")


@app.route("/learn/trusted_systems")
def learn_system():
    return render_template("learn/learn_system.html", title="Learn - Trusted systems and reference monitor")


@app.route("/learn/security_models")
def learn_model():
    return render_template("learn/learn_model.html", title="Learn - Security models")


@app.route("/learn/security_management")
def learn_management():
    return render_template("learn/learn_management.html", title="Learn - Security management practices")


@app.route("/learn/type_attacks")
def learn_attack():
    return render_template("learn/learn_attack.html", title="Learn - Types of attacks")


@app.route("/learn/quiz", methods=["GET", "POST"])
def learn_quiz():
    answered = False
    correct_ans = ["B", ["B", "C", "D"], "C", "effort", "B"]
    if request.method == "POST":
        answered = True
        try:
            ans1 = request.form["q1"].upper()
        except:
            ans1 = "Unanswered"
        try:
            ans2 = request.form.getlist("q2")
            ans2 = [ans.upper() for ans in ans2]
        except:
            ans2 = "Unanswered"
        try:
            ans3 = request.form["q3"].upper()
        except:
            ans3 = "Unanswered"
        try:
            ans4 = request.form["q4"].lower()
        except:
            ans4 = "Unanswered"
        try:
            ans5 = request.form["q5"].upper()
        except:
            ans5 = "Unanswered"
        given_ans = [ans1, ans2, ans3, ans4, ans5]
        result = list(zip(given_ans, correct_ans))
        return render_template("learn/learn_quiz.html", title="Learn - Quiz", answered=answered, result=result)

    return render_template("learn/learn_quiz.html", title="Learn - Quiz", answered=answered)


#
#
#


@app.route("/cryptography")  # Cryptography techniques
def cryptography():
    return render_template("Crypto/cryptography.html", title="Cryptography")


@app.route("/cryptography/shiftcipher", methods=["GET", "POST"])
def cryptography_shiftcipher():
    output = ""
    if request.method == "POST":
        try:
            mode = request.form["mode"]
            chars = request.form["characters"]
            key = int(request.form["key"])
            text = request.form["text"]
            if mode == "encrypt":
                output = shift_cipher.encrypt(key, text, chars)
            elif mode == "decrypt":
                output = shift_cipher.decrypt(key, text, chars)
        except:
            output = "An error have occured! Please refer to the user guide for what may have caused the error."

    return render_template("Crypto/cryptography_shiftcipher.html", title="Crypto - Shift Cipher", output=output)


@app.route("/cryptography/monoalphacipher", methods=["GET", "POST"])
def cryptography_monoalphacipher():
    output = ""
    key = ""
    generated_key_used = False
    if request.method == "POST":
        try:
            mode = request.form["mode"]
            key = request.form["key"]
            if key:
                assert monoalpha_cipher.validate_key(key)
            else:
                assert mode == "encrypt"
                key = monoalpha_cipher.generate_key()
                generated_key_used = True
            text = request.form["text"]
            if mode == "encrypt":
                output = monoalpha_cipher.encrypt(key, text)
            elif mode == "decrypt":
                print("decrypting")
                print(text)
                print(key)
                output = monoalpha_cipher.decrypt(key, text)
                print(output)
        except:
            output = "An error have occured! Please refer to the user guide for what may have caused the error."

    if generated_key_used:
        return render_template("Crypto/cryptography_monoalphacipher.html", title="Crypto - Mono-alphabet Cipher", output=output, output_key=key)
    else:
        return render_template("Crypto/cryptography_monoalphacipher.html", title="Crypto - Mono-alphabet Cipher", output=output)


@app.route("/cryptography/railfencetech",  methods=["GET", "POST"])
def cryptography_railfencetech():
    output = ""
    if request.method == "POST":
        try:
            mode = request.form["mode"]
            rows = int(request.form["row"])
            text = request.form["text"]
            if mode == "encrypt":
                output = railfence_cipher.encrypt(rows, text)
            elif mode == "decrypt":
                output = railfence_cipher.decrypt(rows, text)
        except:
            output = "An error have occured! Please refer to the user guide for what may have caused the error."

    return render_template("Crypto/cryptography_railfencetech.html", title="Crypto - Rail Fence Technique", output=output)


@app.route("/cryptography/coltranstech",  methods=["GET", "POST"])
def cryptography_coltranstech():
    output = ""
    if request.method == "POST":
        try:
            mode = request.form["mode"]
            cols = int(request.form["columns"])
            key = request.form["key"]
            if key:
                assert column_cipher.verify_inputs(cols, key)
            text = request.form["text"]
            if mode == "encrypt":
                output = column_cipher.encrypt(cols, key, text)
            elif mode == "decrypt":
                output = column_cipher.decrypt(cols, key, text)
        except:
            output = "An error have occured! Please refer to the user guide for what may have caused the error."

    return render_template("Crypto/cryptography_coltranstech.html", title="Crypto - Simple Columnar Transposition Technique", output=output)


@app.route("/cryptography/vernamcipher",  methods=["GET", "POST"])
def cryptography_vernamcipher():
    output = ""
    if request.method == "POST":
        try:
            mode = request.form["mode"]
            key = request.form["key"]
            text = request.form["text"]
            assert vernam_cipher.verify_key(key, text)
            if mode == "encrypt":
                output = vernam_cipher.encrypt(key, text)
            elif mode == "decrypt":
                output = vernam_cipher.decrypt(key, text)
        except:
            output = "An error have occured! Please refer to the user guide for what may have caused the error."

    return render_template("Crypto/cryptography_vernamcipher.html", title="Crypto - Vernam Cipher", output=output)


@app.route("/cryptography/dhkeyexchange", methods=["GET", "POST"])
def cryptography_dhkeyexchange():
    output = ""
    if request.method == "POST":
        try:
            n = int(request.form["n"])
            g = int(request.form["g"])
            x = int(request.form["x"])
            y = int(request.form["y"])
            assert dhkey_exchange.is_prime(n)
            assert dhkey_exchange.is_prime(g)
            output = dhkey_exchange.generate_key(n, g, x, y)
        except AssertionError:
            output = "An error have occured! Either 'n' or 'g' is not a prime number."
        except:
            output = "An error have occured! Please refer to the user guide for what may have caused the error."

    return render_template("Crypto/cryptography_dhkeyexchange.html", title="Crypto - Diffie-Hellman Key Exchange", output=output)

#
#
#


@app.route("/symmetric")  # Symmetric algorithms
def symmetric():
    return render_template("symmetric/symmetric.html", title="Symmetric Algorithms")


@app.route("/symmetric/AES", methods=["GET", "POST"])
def symmetric_aes():
    output = ""
    key = ""
    iv = ""
    if request.method == "POST":
        try:
            method = request.form["method"]
            mode = request.form["mode"]

            if method == "encrypt":
                key = int(request.form["key"])
                key = aes.get_random_key(key)
                text = request.form["text"].encode("utf-8")

                if mode == "ECB":
                    output = aes.encrypt_ecb(key, text)
                elif mode == "CBC":
                    iv, output = aes.encrypt_cbc(key, text)
                elif mode == "CFB":
                    iv, output = aes.encrypt_cfb(key, text)
                elif mode == "OFB":
                    iv, output = aes.encrypt_ofb(key, text)

            elif method == "decrypt":
                key = request.form["key"]
                key = aes.convert_to_bin(key)
                iv = request.form["iv"]
                iv = aes.convert_to_bin(iv)
                text = request.form["text"]
                text = aes.convert_to_bin(text)

                if mode == "ECB":
                    output = aes.decrypt_ecb(key, text)
                elif mode == "CBC":
                    output = aes.decrypt_cbc(key, iv, text)
                elif mode == "CFB":
                    output = aes.decrypt_cfb(key, iv, text)
                elif mode == "OFB":
                    output = aes.decrypt_ofb(key, iv, text)

                output = aes.convert_to_str(output)
                return render_template("symmetric/symmetric_aes.html", title="Symmetric Algorithms - AES", output=output)

        except:
            output = "An error have occured! Please refer to the user guide for what may have caused the error."
            return render_template("symmetric/symmetric_aes.html", title="Symmetric Algorithms - AES", output=output)

    output = aes.convert_to_str(output)
    key = aes.convert_to_str(key)
    iv = aes.convert_to_str(iv)
    return render_template("symmetric/symmetric_aes.html", title="Symmetric Algorithms - AES", output=output, key=key, iv=iv)


if __name__ == "__main__":
    app.run(debug=True)
