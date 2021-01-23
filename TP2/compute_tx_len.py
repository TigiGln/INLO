#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Ce code peut être réutilisé pour différents fichiers GTF"""
import re
transcript_start = dict()
transcript_end = dict()
def get_tx_genomic_length(input_file=None):
    """Cette fonction sert à récupérer les positions de chaque transcript"""
    file_handler = open(input_file)
    for line in file_handler:
        token = line.split("\t")
        start = int(token[3]) #le début de l'élément courant
        end = int(token[4]) #la fin de l'élément courant
    tx_id = re.search('transcript_id "([^"]+)"', token[8]).group(1) #L'identifiant du transcrit
    if tx_id not in transcript_start:
        transcript_start[tx_id] = start
        transcript_end[tx_id] = end
    else:
        if start < transcript_start[tx_id]:
            transcript_start[tx_id] = start
        if end > transcript_end[tx_id]:
            transcript_end[tx_id] = end
    for tx_id in transcript_start:
        print(tx_id + "\t" + str(transcript_end[tx_id] - transcript_start[tx_id] + 1))
if __name__ == '__main__':
    get_tx_genomic_length(input_file='../pymetacline/data/gtf/simple.gtf')
    