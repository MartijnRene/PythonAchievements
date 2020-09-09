>>> 2+2
4
>>> 3*10
30
>>> 100-10
90
>>> 25/5
5.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> print('Mijn naam is Martijn')
Mijn naam is Martijn
>>> naam = 'Martijn'
>>> print(naam)
Martijn
>>> print(naam.upper())
MARTIJN
>>> print(naam[0:2])
Ma
>>> print(naam[::-1])
njitraM
>>> leeftijd = 24
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Martijn ben je al 24 jaar?
>>> leeftijd = leeftijd+1
>>> leeftijd
25
>>> leeftijd = leeftijd-1
>>> leeftijd
24
>>> if leeftijd < 18:
...  hoelang_tot18jaar = 18 - leeftijd
...  print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...  hoelang_al18jaar = leeftijd - 18
...  print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...  print('Je bent precies ' + str(leeftijd) + ' jaar')
...
Het is alweer 6 jaar geleden dat je 18 werd ;-)
>>> from random import randint
>>> randint(0,1000)
752
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
564
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 931
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 12:07:05.424002
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'