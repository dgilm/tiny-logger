import sys
import xapian

class Search:

    def __init__(self, db_path):
        self.db_path = db_path
    
    def search(self, query):
        try:
            # Open the database for searching.
            database = xapian.Database(self.db_path)

            # Start an enquire session.
            enquire = xapian.Enquire(database)

            # Combine the rest of the command line arguments with spaces
            # between them, so that simple queries don't have to be quoted at
            # the shell level
            query_string = str.join(' ', query)

            # Parse the query string to produce a Xapian::Query object.
            qp = xapian.QueryParser()
            stemmer = xapian.Stem("english")
            qp.set_stemmer(stemmer)
            qp.set_database(database)
            qp.set_stemming_strategy(xapian.QueryParser.STEM_SOME)
            query = qp.parse_query(query_string,
                                   xapian.QueryParser.FLAG_WILDCARD)
            print "Parsed query is: %s" % str(query)

            # Find the top 10 results for the query.
            enquire.set_query(query)
            matches = enquire.get_mset(0, 10)

            # Display the results.
            print "%i results found." % matches.get_matches_estimated()
            print "Results 1-%i:" % matches.size()

            for m in matches:
                print "%i: %i%% docid=%i [%s]" % \
                    (m.rank + 1, m.percent, m.docid, m.document.get_data())

        except Exception, e:
            print >> sys.stderr, "Exception: %s" % str(e)
            sys.exit(1)    
    
if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: %s QUERY_TO_SEARCH" % sys.argv[0]
        sys.exit(1)
    
    search = Search("/tmp/xapian-db")
    search.search(sys.argv[1:])
    
