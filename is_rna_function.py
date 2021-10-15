def is_rna(seq):
    bases = "ACGTU"
    uracile = 'U'
    thymine = 'T'
    if uracile in seq :
        print("True")
    elif thymine in seq:
        print("DNA")
    else:
        print("Don't know")






