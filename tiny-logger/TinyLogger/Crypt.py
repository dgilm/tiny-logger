## Cryptographic signature and verification of messages

import sys
import hashlib

from FileUtils import FileUtils


class Crypt:

    def __init__(self, crypto_algorithm, secret_shared_key):
        self.crypto_algorithm = getattr(hashlib, crypto_algorithm)
        self.secret_shared_key = secret_shared_key

    def digest(self, filename):
        """ generate a cryptographic hash of the actual data
            combined with a shared secret key """
        stream = FileUtils.get_stream(filename)
        digest = self.crypto_algorithm()
        digest.update(self.secret_shared_key)
        digest.update(stream)
        return digest.hexdigest()

    def sign_file(self, input_):
        print "Cryptographic signature of file [%s]:" % (input_),
        try:
            # python 2.6
            # with open(input_ + ".sign", 'w') as foutput:
            signature = self.digest(input_)
            foutput = open(input_ + ".sign", 'w')
            foutput.write(signature)
            foutput.close()
            return signature
        except IOError, e_msg:
            print e_msg
            sys.exit(1)

    def validate(self, input_, signature):
        try:
            result = self.digest(input_) == file(signature).read()
        except IOError, e_msg:
            print e_msg
            sys.exit(1)

        return result
