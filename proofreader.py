# automated proofreader in python

import lmproof
def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print(f"Original text is {text}")
    print(f"Proofread text is {correction}")

proofread("Correct Mee")