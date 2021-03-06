#!/usr/bin/env python3
#-*- coding : utf8 -*-

import unittest

from others import *

class TestStats(unittest.TestCase):

    def test_dot_text_files_from_folder_as_list(self):
        dossier_corpus = CORPUS_TEST_ROOT
        liste_fichiers = list_text_in_folder_as_list(dossier_corpus)

        self.assertIsInstance(liste_fichiers, list)

    def test_import_text_as_one_string(self):
        dossier_corpus = CORPUS_TEST_ROOT
        liste_fichiers = list_text_in_folder_as_list(dossier_corpus)

        for fichier in liste_fichiers :
            a = os.path.join(dossier_corpus, fichier)
            b = import_text_as_one_string(a)

            self.assertIsInstance(b, str)



    # def test_import_text_as_list_of_strings(self):
    #     dossier_corpus = CORPUS_TEST_ROOT
    #     texte = None
    #
    #     liste_fichiers = os.listdir(dossier_corpus)
    #
    #     if len(liste_fichiers) > 2 :
    #         texte_1 = import_text_as_list_of_strings(os.path.join(dossier_corpus, liste_fichiers[1]))
    #         self.assertIsInstance(texte_1 , list)
    #
    #         texte_2 = import_text_as_list_of_strings(os.path.join(dossier_corpus, liste_fichiers[2]))
    #         self.assertIsInstance(texte_2 , list)

        # for fichier in os.listdir(dossier_corpus) :
        #     #On ne veut que les fichiers textes
        #     if fichier.endswith('.txt') :
        #         # on les importe : on veut que ce soit des listes
        #         texte = import_text_as_list_of_words(os.path.join(dossier_corpus, fichier))
        #         # on verifie
        #         self.assertIsInstance(texte, list)


    # def test_import_text_as_list_of_words(self):
    #     dossier_corpus = CORPUS_TEST_ROOT
    #     texte = None
    #
    #     liste_fichiers = os.listdir(dossier_corpus)
    #
    #     if len(liste_fichiers) > 2 :
    #         texte_1 = import_text_as_list_of_words(os.path.join(dossier_corpus, liste_fichiers[1]))
    #         self.assertIsInstance(texte_1 , list)
    #
    #         texte_2 = import_text_as_list_of_words(os.path.join(dossier_corpus, liste_fichiers[2]))
    #         self.assertIsInstance(texte_2 , list)

        # for fichier in os.listdir(dossier_corpus) :
        #     if fichier.endswith('.txt') :
        #         texte = import_text_as_list_of_words(os.path.join(dossier_corpus, fichier))
        #         self.assertIsInstance(texte, list)


if __name__ == '__main__':
    unittest.main()
