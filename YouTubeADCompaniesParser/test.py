import matplotlib.pyplot as plt


domain_names_count = {'protonvpn.com': 1, 'alegotour.com': 1, 'weber.com': 1, 'kion.ru': 1,  'navzvade.ru': 1, 'sardayal.ru': 1, 'seloglazok.ru': 1, 'bolshayakocha.ru': 1, 'khrug.ru': 1, 'tarusa.city': 1, 'shalash.academy': 1, 'kolya.vsigarev.ru': 1, 'cian.ru': 1, 'shop.tastycoffee.ru': 1, 'ozerov.ru': 1, 'kommersant.ru': 1, 'evanetwork.ru': 1, 'showroom.hyundai.ru': 1, 'mobility.hyundai.ru': 1, 'etniq.ru': 1, 'coptertime.ru': 1, 'livefest.ru': 1, 'gmig.ru': 1, 'kazan.fitauto.ru': 1, 'renins.ru': 1, 'school.skyeng.ru': 1, 'mcgheela.com': 1, 'stasnamin.ru': 1, 'ria.ru': 1, 'mxat.ru': 1, 'alisa.net': 1, 'zavidnoe-club.com': 1, 'limonov-eduard.livejournal.com': 1, 'glavclub.com': 1, 'acer.com': 1, '2119.ru': 1, 'bestwatch.ru': 1, 'ostrovok.ru': 1, 'roizmanfond.ru': 1, 'okko.tv': 1, 'askona.ru': 1, 'carprice.ru': 1, 'growfood.pro': 1, 'icondesigne.ru': 1, 'barbershowrussia.com': 1, 'qlean.ru': 1, 'gradnja.ru': 1, 'letu.ru': 2, 'ozon.ru': 2, 'online.synchronize.ru': 2,   'kinopoisk.ru': 2, 'vive.com': 2, 'sibircollection.ru': 2, 'htc-online.ru': 2, 'skysmart.ru': 3, 'ek.ua': 4, 'alfabank.ru': 4, 'hyundai.ru': 5, 'hd.kinopoisk.ru': 6, 'sports.ru': 7, 'storytel.com': 8, 'kzn.profi.ru': 8, 'skyeng.ru': 8, 'aviasales.ru': 15}
# VDud
y = list(domain_names_count.keys())

# getting values against each value of y
x = list(domain_names_count.values())
plt.barh(y, x)

# setting label of y-axis
plt.ylabel("Domain Names")

# setting label of x-axis
plt.xlabel("Domain Names Count")
plt.title("VDud Advertisment Company Analize")


plt.show()