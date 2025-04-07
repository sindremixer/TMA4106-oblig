import numpy as np
import matplotlib.pyplot as plt

x = [0.025,0.05,0.075,0.1,0.125,0.15] #konsentrasjon
y = [0.1234,0.2463,0.3713,0.4971,0.6378,0.7454] #absorbsjon

prøve = 0.4004 #absorbsjon av ukjent konsentrasjon

x_mean = 0
y_mean = 0
xTy = 0
x_len = 0

for i in range(6):
    x_mean += x[i]
    y_mean += y[i]
    xTy += x[i]*y[i]
    x_len += x[i]**2

x_mean = x_mean/6
y_mean = y_mean/6
x_len = np.sqrt(x_len)


beta_1 = (xTy - 6*x_mean*y_mean)/(x_len**2-6*(x_mean**2))
beta_0 = y_mean - beta_1*x_mean

x_akse = np.linspace(0,0.2,100)

def reg(x_akse,beta_1,beta_0):
    return beta_1*x_akse + beta_0

ukjent_kons = (0.4004-beta_0)/beta_1
print(ukjent_kons)
print(beta_0)
print(beta_1)
plt.plot(x_akse,reg(x_akse,beta_1,beta_0))
plt.plot(x,y,"o")
plt.show()