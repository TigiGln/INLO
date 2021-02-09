# INLO

TP5: test unitaire sur les méthodes de la classe LinkedList



(base) thierry@thierry-HP:~/cours_master_DLAD/semestre_2/Ingénieurie_logicielle/
INLO/TP5/test_unitaire$ pylint test_linkedlist.py --py3k --enable=all --disable=print-statement,no-absolute-import

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.21/10, +1.79)

Le pylint est à 10/10, si on met la commande sys.path.append("..") après l'import du module linkedList. Cependant python n'arrive pas à trouver le module car le fichier linkedList est dans le dossier parent.
Si je met sys.path.append("..") avant l'import du module linkedList, le pylint passe à 9.62/10:

(base) thierry@thierry-HP:~/cours_master_DLAD/semestre_2/Ingénieurie_logicielle/
INLO/TP5/test_unitaire$ pylint test_linkedlist.py --py3k --enable=all --disable=print-statement,no-absolute-import
************* Module test_linkedlist
test_linkedlist.py:11:0: C0413: Import "import linkedList" should be placed at the top of the module (wrong-import-position)

-------------------------------------------------------------------
Your code has been rated at 9.62/10 (previous run: 10.00/10, -0.38)

Je n'arrive donc pas à avoir un pylint à 10/10 et un code fonctionnel si je mets le fichier test_linkedlist.py dans un sous répertoire test.


Dans le même répertoire, le pylint:

(base) thierry@thierry-HP:~/cours_master_DLAD/semestre_2/Ingénieurie_logicielle/
INLO/TP5$ pylint test_linkedlist.py --py3k --enable=all --disable=print-statement,no-absolute-import

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.23/10, +0.77)

