#!/usr/bin/env python3
#-*-coding: utf-8 -*-
"""
author: Thierry Galliano
"""
import argparse
PROGRAM_DESCRIPTION = """
My program takes a fasta DNA sequence file as input and
searches for specific identifiers using the seq argument.
Returns us the sequences of these identifiers
-inputfile takes the path of the input file
-seq takes the list of required identifiers
"""
def create_parser():
    """
    This function is used to create the arguments for
    launching the execution of the program
    """
    parser = argparse.ArgumentParser(add_help = True,
                                     description = PROGRAM_DESCRIPTION)
    parser.add_argument('-i','--inputfile',
                        type = argparse.FileType("r"),
                        help = "Path to file",
                        metavar = "Fasta",
                        required = True)
    parser.add_argument('-seq','--sequence',
                        help = "sequence identifier list",
                        type = str,
                        nargs = "+",
                        required = True
                        )
    return parser
def read_fasta_file():
    """
    This function allows you to select the sequences of interests
    according to the arguments entered
    """
    parser = create_parser()
    args = parser.parse_args()#méthode pour appliquer les parser
    inputfile = args.inputfile
    ids_sequences = args.sequence
    dico_fasta = dict()
    keep_fasta = False
    with inputfile as file_fasta:
        for line in file_fasta:
            if not line.isspace():
                if line.startswith(">"):
                    id_seq = line[1:len(line)].strip()
                    keep_fasta = id_seq in ids_sequences
                else:
                    if keep_fasta:
                        dico_fasta[id_seq] = line.strip()
    for id_sequence, sequence in dico_fasta.items():
        print(id_sequence + ": \n" + sequence + "\n")
if __name__ == "__main__":
    read_fasta_file()
    #if the program is not started by an annex program then it is started by
    #itself thanks to this condition
    