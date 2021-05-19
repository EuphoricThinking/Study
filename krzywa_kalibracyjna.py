import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

import math

if __name__ == '__main__':
    masa_w_kDa = [200, 116, 97, 66, 45, 31, 21]
    rzezba_w_cm = [0.4, 0.8, 0.95, 1.4, 2.2, 3.5, 4.7]
    masa_log = [math.log(i, 10) for i in masa_w_kDa]

    interpolacja = interp1d(rzezba_w_cm, masa_log)
    plt.plot(rzezba_w_cm, masa_log, 'bX-', label = 'Wzorzec')
    plt.plot(1.55, interpolacja(1.55), 'ro', label = 'Albumina')
    plt.plot(2.0, interpolacja(2.0), 'go', label = 'Ciężki łańcuch przeciwciał')
    plt.plot(3.8, interpolacja(3.8), 'yo', label = 'Lekki łańcuch przeciwciał')
    plt.ylabel("Logarytm dziesiętny masy [kDa]")
    plt.xlabel('Migracja w centymetrach')
    plt.title('Krzywa kalibracyjna do wyznaczania masy cząsteczkowej białka')
    plt.legend()
    plt.show()
    plt.savefig('/home/heheszek/Downloads/Krzywa_kalibracyjna.png')
    #print(math.log(100,10))


