from reguly import Zbior_Regul

sloneczna = 'sloneczna'
pochmurna = 'pochmurna'
deszczowa = 'deszczowa'
zimna = 'zimna'
umiarkowana = 'umiarkowana'
ciepla = 'ciepla'
normalna = 'normalna'
duza = 'duza'
slaby = 'slaby'
silny = 'silny'
selektor_aura_ogolny = [sloneczna, pochmurna, deszczowa]
selektor_temperatura_ogolny = [zimna, umiarkowana, ciepla]
selektor_wilgotnosc_ogolny = [normalna, duza]
selektor_wiatr_ogolny = [slaby, silny]

kompleks_pogoda_ogolny = [selektor_aura_ogolny, selektor_temperatura_ogolny, selektor_wilgotnosc_ogolny, selektor_wiatr_ogolny]

selektor_aura_1 = sloneczna
selektor_temperatura_1 = ciepla
selektor_wilgotnosc_1 = duza
selektor_wiatr_1 = slaby

selektor_aura_2 = sloneczna
selektor_temperatura_2 = ciepla
selektor_wilgotnosc_2 = duza
selektor_wiatr_2 = silny

selektor_aura_3 = pochmurna
selektor_temperatura_3 = ciepla
selektor_wilgotnosc_3 = duza
selektor_wiatr_3 = slaby

selektor_aura_4 = deszczowa
selektor_temperatura_4 = umiarkowana
selektor_wilgotnosc_4 = duza
selektor_wiatr_4 = slaby

selektor_aura_5 = deszczowa
selektor_temperatura_5 = zimna
selektor_wilgotnosc_5 = normalna
selektor_wiatr_5 = slaby

selektor_aura_6 = deszczowa
selektor_temperatura_6 = zimna
selektor_wilgotnosc_6 = normalna
selektor_wiatr_6 = silny

selektor_aura_7 = pochmurna
selektor_temperatura_7 = zimna
selektor_wilgotnosc_7 = normalna
selektor_wiatr_7 = silny

selektor_aura_8 = sloneczna
selektor_temperatura_8 = umiarkowana
selektor_wilgotnosc_8 = duza
selektor_wiatr_8 = slaby

selektor_aura_9 = sloneczna
selektor_temperatura_9 = zimna
selektor_wilgotnosc_9 = normalna
selektor_wiatr_9 = slaby

selektor_aura_10 = deszczowa
selektor_temperatura_10 = umiarkowana
selektor_wilgotnosc_10 = normalna
selektor_wiatr_10 = slaby

selektor_aura_11 = sloneczna
selektor_temperatura_11 = umiarkowana
selektor_wilgotnosc_11 = normalna
selektor_wiatr_11 = silny

selektor_aura_12 = pochmurna
selektor_temperatura_12 = umiarkowana
selektor_wilgotnosc_12 = duza
selektor_wiatr_12 = silny

selektor_aura_13 = pochmurna
selektor_temperatura_13 = ciepla
selektor_wilgotnosc_13 = normalna
selektor_wiatr_13 = slaby

selektor_aura_14 = deszczowa
selektor_temperatura_14 = umiarkowana
selektor_wilgotnosc_14 = duza
selektor_wiatr_14 = silny

kompleks_1 = [selektor_aura_1, selektor_temperatura_1, selektor_wilgotnosc_1, selektor_wiatr_1]
kompleks_2 = [selektor_aura_2, selektor_temperatura_2, selektor_wilgotnosc_2, selektor_wiatr_2]
kompleks_3 = [selektor_aura_3, selektor_temperatura_3, selektor_wilgotnosc_3, selektor_wiatr_3]
kompleks_4 = [selektor_aura_4, selektor_temperatura_4, selektor_wilgotnosc_4, selektor_wiatr_4]
kompleks_5 = [selektor_aura_5, selektor_temperatura_5, selektor_wilgotnosc_5, selektor_wiatr_5]
kompleks_6 = [selektor_aura_6, selektor_temperatura_6, selektor_wilgotnosc_6, selektor_wiatr_6]
kompleks_7 = [selektor_aura_7, selektor_temperatura_7, selektor_wilgotnosc_7, selektor_wiatr_7]
kompleks_8 = [selektor_aura_8, selektor_temperatura_8, selektor_wilgotnosc_8, selektor_wiatr_8]
kompleks_9 = [selektor_aura_9, selektor_temperatura_9, selektor_wilgotnosc_9, selektor_wiatr_9]
kompleks_10 = [selektor_aura_10, selektor_temperatura_10, selektor_wilgotnosc_10, selektor_wiatr_10]
kompleks_11 = [selektor_aura_11, selektor_temperatura_11, selektor_wilgotnosc_11, selektor_wiatr_11]
kompleks_12 = [selektor_aura_12, selektor_temperatura_12, selektor_wilgotnosc_12, selektor_wiatr_12]
kompleks_13 = [selektor_aura_13, selektor_temperatura_13, selektor_wilgotnosc_13, selektor_wiatr_13]
kompleks_14 = [selektor_aura_14, selektor_temperatura_14, selektor_wilgotnosc_14, selektor_wiatr_14]
przyklad_1 = kompleks_1 + [1]
przyklad_2 = kompleks_2 + [0]
przyklad_3 = kompleks_3 + [1]
przyklad_4 = kompleks_4 + [1]
przyklad_5 = kompleks_5 + [1]
przyklad_6 = kompleks_6 + [0]
przyklad_7 = kompleks_7 + [1]
przyklad_8 = kompleks_8 + [0]
przyklad_9 = kompleks_9 + [1]
przyklad_10 = kompleks_10 + [1]
przyklad_11 = kompleks_11 + [1]
przyklad_12 = kompleks_12 + [1]
przyklad_13 = kompleks_13 + [1]
przyklad_14 = kompleks_14 + [0]

zbior_k = [kompleks_1, kompleks_2]
zbior_l = [kompleks_3, kompleks_4]

zbior_T = [przyklad_1, przyklad_2, przyklad_3, przyklad_4, przyklad_5, przyklad_6, przyklad_7, przyklad_8, przyklad_9, przyklad_10, przyklad_11, przyklad_12, przyklad_13, przyklad_14]
zbior_P = [przyklad_1, przyklad_2, przyklad_3, przyklad_4, przyklad_5, przyklad_6, przyklad_7, przyklad_8, przyklad_9, przyklad_10, przyklad_11, przyklad_12, przyklad_13, przyklad_14]

Reguly = Zbior_Regul(zbior_P, kompleks_pogoda_ogolny)
print(Reguly.zbior_Regul)
print(len(Reguly.zbior_Regul))
