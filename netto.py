def netto_value(brutto, tax):
    netto = brutto / (1 + tax)
    return round(netto, 2)

