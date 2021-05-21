import matplotlib.pyplot as plt
import scipy.interpolate as sc

def pokaz_wykres(glukoza_mg, absorbancja, xlab, ylab, upper_title, grafika):
    plt.plot(glukoza_mg, absorbancja, grafika)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(upper_title)
    plt.grid()
    plt.show()

def zawartosc_cukrow_redukujacych(absorbancja, glukoza_mg_treningowe, absorbancja_treningowa):
    interpolacja_absorbancja = sc.interp1d(absorbancja_treningowa, glukoza_mg_treningowe)
    for i in range(len(absorbancja)):
        print(round(float(interpolacja_absorbancja(absorbancja[i])), 4))

if __name__ == '__main__':
    x_label = "Zawartość glukozy w próbie [mg]"
    y_label = "Absorbancja"
    title = "Krzywa wzorcowa zawartości glukozy"

    zawartosc_glukozy_mg = [0, 0.2, 0.4, 0.6, 0.8, 1.2, 1.6]
    absorbancja_wzorzec = [0, 0.042, 0.154, 0.265, 0.411, 0.664, 0.898]
    absorbancja_proby = [0.079, 0.159, 0.247, 0.275, 0.516, 0.674, 0.281, 0.344, 0.474]
    cukry_redukujace = [0, 2.95, 22.7, 31.53, 34.1, 53.62, 67.55, 69.05, 78.6, 99.86]
    czas_inkubacji = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    #pokaz_wykres(zawartosc_glukozy_mg, absorbancja_wzorzec, x_label, y_label, title, 'bo--')
    pokaz_wykres(czas_inkubacji, cukry_redukujace, 'Czas inkubacji [min]', 'Stężenie cukrów redukujących [mM]',
                 'Stężenie cukrów redukujących w czasie inkubacji', 'ro--')
    
    zawartosc_cukrow_redukujacych(absorbancja_proby, zawartosc_glukozy_mg, absorbancja_wzorzec)




