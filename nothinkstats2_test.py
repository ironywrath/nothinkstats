import numpy as np

import nothinkstats2 as nt2

#pct = nt2.ParetoCdfTest()
#pct.xs = pct.LinspaceTest(5000, 1e7, 50)

#print(nt2.LinespaceTest(1,100,10))

#xs = nt2.LinespaceTest(1,100,10)

'''
print('Linspace:')
print(pct.xs)
print('\n')

print('xs/min')
print(pct.ParetoCdfTest1(5000,1))
print('\n')

print("(xs/min)** alpha")
print(pct.ParetoCdfTest2(5000, 1.4))
print(pct.ParetoCdfTest2(5000, 2))
print('\n')

print("(xs/min)** -alpha")
print(pct.ParetoCdfTest3(5000, 1.4))
print(pct.ParetoCdfTest3(5000, 2))
print('\n')

print("1 - (xs/min)** -alpha")
print(pct.ParetoCdfTest4(5000, 1.4))
print(pct.ParetoCdfTest4(5000, 2))
print('\n')

'''
print('e 1: ', np.exp(1))
print('\n')

#print(nt2.RenderExpoCdf(2, 0, 100, 100))
xs = np.linspace(0, 3.0, 50)
print(xs)
print('\n')
for item in xs:
    mu_Result = -8 * item
    print('-8 X', item, '=', mu_Result)
    print('e exponent result: ', np.exp(mu_Result))
    print('1- result: ', 1-np.exp(mu_Result))
    print('----------------------------------')






