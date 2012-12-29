import sys
import xapian

import FileUtils

class Index:

    def __init__(self, db_path):
        self.db_path = db_path

    def index(self, filename):
        # Open the database for update, creating a new database if necessary
        database = xapian.WritableDatabase(self.db_path, 
                                           xapian.DB_CREATE_OR_OPEN)

        indexer = xapian.TermGenerator()
        stemmer = xapian.Stem("english")
        indexer.set_stemmer(stemmer)

        doc = xapian.Document()
        stream = FileUtils.FileUtils.get_stream(filename)
        doc.set_data(stream)
        indexer.set_document(doc)
        indexer.index_text(stream)
        database.add_document(doc)
    

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: %s FILE_TO_INDEX" % sys.argv[0]
        sys.exit(1)
    
    indexer = Index("/tmp/xapian-db")
    indexer.index(sys.argv[1])

