# packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# population parameters (you can change it as you want)
a = 5
b = 36/1000

# number of simulations (you can change it too)
sim = 100

# generating "fixed" data
id = np.array(list(range(1, 1001, 1)))
x = np.random.RandomState(42) # set seed for X
x = np.array(x.normal(50, 15, 1000))

# auxiliary lists to save the results of each following estimation
aux_b_hat = []
aux_a_hat = []

# loooooooooooooping (or just the "monte carlo simulation")
for sim in range(1, sim, 1):
    
    # generating a new error term for each iteration and re-calculating y
    u = np.array(np.random.normal(0, 1, 1000)) # here, you can force a correlation between u and x (ommited variable bias)
    y = a + (b * x) + u

    # final dataframe
    data = np.column_stack((id, x, u, y))

    # important math
    x_diff = data[:, 1] - np.mean(data[:, 1]) # xi - xbar
    x_diff_sqr = x_diff ** 2 # (xi - xbar) ^ 2

    y_diff = data[:, 3] - np.mean(data[:, 3]) # yi - ybar
    y_diff_sqr = y_diff ** 2 # (yi - ybar) ^ 2

    x_y = x_diff * y_diff # (xi - xbar) * (yi - ybar)

    # final sums
    sum_x_y = np.sum(x_y)
    sum_x_diff_sqr = np.sum(x_diff_sqr)

    # finally, the estimated parameters!
    b_hat = sum_x_y / sum_x_diff_sqr
    a_hat = np.mean(data[:, 3]) - b_hat * np.mean(data[:, 1])

    # appending the results of each simulation
    aux_b_hat.append(b_hat)
    aux_a_hat.append(a_hat)

# hmmmmmmmmm means
print(round(np.mean(aux_b_hat), 5))
print(round(np.mean(aux_a_hat), 5))

# graph
sns_plot = sns.displot(aux_b_hat) # dist
plt.axvline(np.mean(aux_b_hat), linestyle = "--", color = "red") # estimated parameter
plt.axvline(0.036, linestyle = "-", color = "black") # population parameter
plt.legend(("est. param.", "pop. param."))
sns_plot.savefig("listas_econometria\lista1\output_mc_beta.png") # saving