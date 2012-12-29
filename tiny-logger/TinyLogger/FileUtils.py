import datetime
import os


class FileUtils:
    """Utility compress functions for stream reader"""

    @staticmethod
    def get_stream(filename):

        if filename.endswith('.bz2'):
            import bz2
            return bz2.decompress(file(filename).read())

        elif filename.endswith('.gz'):
            import gzip
            f = gzip.open(filename, 'rb')
            f_content = f.read()
            f.close()
            return f_content

        else:
            # IOError will be trigger if file is compressed whit other
            # compress method than gzip or bzip
            # rar, lzma, etc. are still not supported
            return file(filename).read()

    @staticmethod
    def get_dir_to_write(prefix='/var/log/tiny-logger/'):
        curdate = datetime.datetime.now()
        for p in [(prefix,
                   curdate.strftime("%Y"),
                   curdate.strftime("%m"),
                   curdate.strftime("%d"),
                   curdate.strftime("%H"))]:
            return os.path.join(*p)
