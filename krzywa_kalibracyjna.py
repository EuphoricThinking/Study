import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import math

def logarytmowane(masa_log, rzezba_w_cm):
    interpolacja = interp1d(rzezba_w_cm, masa_log)
    plt.plot(rzezba_w_cm, masa_log, 'bX-', label='Wzorzec')
    plt.plot(1.55, interpolacja(1.55), 'ro', label='Albumina')
    plt.plot(2.0, interpolacja(2.0), 'go', label='Ciężki łańcuch przeciwciał')
    plt.plot(3.8, interpolacja(3.8), 'yo', label='Lekki łańcuch przeciwciał')
    plt.ylabel("Logarytm dziesiętny masy [kDa]")
    plt.xlabel('Migracja w centymetrach')
    plt.title('Krzywa kalibracyjna do wyznaczania masy cząsteczkowej białka')
    plt.legend()
    plt.show()

def bez_logarytmu(masa, rzezba):
    plt.plot(rzezba, masa, 'bX-')
    plt.show()

if __name__ == '__main__':
    masa_w_kDa = [200.0, 116.0, 97.0, 66.0, 45.0, 31.0, 21.0]
    rzezba_w_cm = [0.4, 0.8, 0.95, 1.4, 2.2, 3.5, 4.7]
    masa_log = [math.log(i, 10) for i in masa_w_kDa]
    masa_logn = [math.log(i) for i in masa_w_kDa]

    interpolacja = interp1d(rzezba_w_cm, masa_log)

    albumina = interpolacja(1.55)
    ciezki_lancuch = interpolacja(2.0)
    lekki_lancuch = interpolacja(3.8)

    text = 'Albumina 1,55 cm: ' + str(round(pow(10, albumina), 2)) + ', ciężki łańcuch 2 cm: ' + str(round(pow(10, ciezki_lancuch), 2)) + ', lekki łańcuch: ' + str(round(pow(10, lekki_lancuch)))
    logarytmowane(masa_log, rzezba_w_cm)
    print(text)
    plt.savefig('/home/heheszek/Downloads/Krzywa_kalibracyjna.png')

