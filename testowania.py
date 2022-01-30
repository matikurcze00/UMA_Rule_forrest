def dokladnosc(funkcja, zbior, kompleks_ogolny):
    nr_odpowiedzi = len(kompleks_ogolny)
    dobrze = 0
    for przyklad in zbior:
        if(przyklad[nr_odpowiedzi] == funkcja.klasyfikacja(przyklad)):
            dobrze += 1
    return(dobrze*100/len(zbior))


def dane_statystyczne(funkcja, zbior, kompleks_ogolny):
    nr_odpowiedzi = len(kompleks_ogolny)
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    TPR = 0
    FPR = 0
    Precyzja = 0
    for przyklad in zbior:
        if(przyklad[nr_odpowiedzi] == 0 and funkcja.klasyfikacja(przyklad) == 0):
            TN += 1
        elif(przyklad[nr_odpowiedzi] == 1 and funkcja.klasyfikacja(przyklad) == 0):
            FN += 1
        elif(przyklad[nr_odpowiedzi] == 1 and funkcja.klasyfikacja(przyklad) == 1):
            TP += 1
        elif(przyklad[nr_odpowiedzi] == 0 and funkcja.klasyfikacja(przyklad) == 1):
            FP += 1
    if (TP + FN) > 0:
        TPR = (TP)/(TP + FN)
    if (FP + TN) > 0:
        FPR = (FP)/(FP + TN)
    if (TP+FP) > 0:
        Precyzja = (TP)/(TP+FP)
    return TPR, FPR, Precyzja
