import sys

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print( "Usage: python conver.py infile outfile column1 column2" )
        exit(-1)

    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    col1 = int(sys.argv[3])
    col2 = int(sys.argv[4])

    inf = open(infilename, "r", encoding="utf-16")
    outf = open(outfilename, "w", encoding="utf-16")

    textlist = inf.readlines()

    for l in textlist:
        l = l.replace('"', '')
        ll = l.split("\t")
        ol = "    " + ll[col1] + " \"" + ll[col2] + "\"\n"
        outf.write(ol)

    inf.close()
    outf.close()

