#!/usr/bin/env python3
#-*- coding : utf8 -*-

import os

import modules.ponctuation_texte as ponctuation_texte
import modules.stats_1_base as stats_base

from settings import PROJECT_ROOT

print(PROJECT_ROOT)

def main():
    print("Salut friend")
    print("go")

# while 1 :
    # a = input("\nLevel 0 : How do you want me to work ? " + \
    #     "\n 1 : Choice 1" + \
    #     "\n 2 : Choice 2" + \
    #     "\n (enter) - Exit" + \
    #     "\nYour choice : ")
    #
    # #==================================
    # if a.strip() == '1' :
    #     print("Choice 1.")
#         break
#     #==================================
#     elif a.strip() == '2' :
#         print("Choice 2.")
#         break #continue pour revenir
#
#     #==================================
#     elif a.strip() == '' :
#         print("\n+++++++++++++++++++++++++++++")
#         print("Thank you ! Bye.")
#         print("+++++++++++++++++++++++++++++\n")
#
#         break
#
#     #==================================
#     else :
#         print("\n-----------------------------------")
#         print("I dont know what to do. (Restart level 0).")
#         print("-----------------------------------")
#

if __name__ == '__main__':
    main()
