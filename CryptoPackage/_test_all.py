from CryptoPackage import shift_cipher_test
from CryptoPackage import monoalpha_cipher_test
from CryptoPackage import railfence_cipher_test
from CryptoPackage import column_cipher_test
from CryptoPackage import vernam_cipher_test
from CryptoPackage import dhkey_exchange_test
from CryptoPackage import aes_test


def run_test():
    shift_cipher_test.run_test()
    monoalpha_cipher_test.run_test()
    railfence_cipher_test.run_test()
    column_cipher_test.run_test()
    vernam_cipher_test.run_test()
    dhkey_exchange_test.run_test()
    aes_test.run_test()


if __name__ == "__main__":
    run_test()
