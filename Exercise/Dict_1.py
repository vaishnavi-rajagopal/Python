
#3.12. Make a French-to-English dictionary called f2e from e2f. Use the items method.

#3.13. Using f2e, print the English equivalent of the French word chien.

#3.14. Make and print a set of English words from the keys in e2f.

e2f={"dog":"chien","cat":"chat","walrus":"morse"}


eng = tuple(e2f.keys())

french = tuple(e2f.values())

f2e = dict(zip(french,eng))

print(f2e)