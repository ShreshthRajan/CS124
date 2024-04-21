import matplotlib.pyplot as plt
import numpy as np
import statistics

with open('kk_results.txt', 'r') as f:
    kk_results = f.read().splitlines()

with open('rr_results.txt', 'r') as f:
    rr_results = f.read().splitlines()

with open('hc_results.txt', 'r') as f:
    hc_results = f.read().splitlines()

with open('sa_results.txt', 'r') as f:
    sa_results = f.read().splitlines()

with open('par_rr_results.txt', 'r') as f:
    par_rr_results = f.read().splitlines()

with open('par_hc_results.txt', 'r') as f:
    par_hc_results = f.read().splitlines()

with open('par_sa_results.txt', 'r') as f:
    par_sa_results = f.read().splitlines()

kk_results = kk_results[2:]
# kk_results = kk_results.replace("e-05", "*10 {-5}")
kk_residues = []
kk_times = []
for i in range(len(kk_results)):
    object = kk_results[i].split(",")
    kk_residues.append(int(object[0]))
    kk_times.append(float(object[1]))

rr_results = rr_results[2:]
rr_residues = []
rr_times = []
for i in range(len(rr_results)):
    object = rr_results[i].split(",")
    rr_residues.append(int(object[0]))
    rr_times.append(float(object[1]))

hc_results = hc_results[2:]
hc_residues = []
hc_times = []
for i in range(len(hc_results)):
    object = hc_results[i].split(",")
    hc_residues.append(int(object[0]))
    hc_times.append(float(object[1]))


sa_results = sa_results[2:]
sa_residues = []
sa_times = []
for i in range(len(sa_results)):
    object = sa_results[i].split(",")
    sa_residues.append(int(object[0]))
    sa_times.append(float(object[1]))

par_rr_results = par_rr_results[2:]
par_rr_residues = []
par_rr_times = []
for i in range(len(par_rr_results)):
    object = par_rr_results[i].split(",")
    par_rr_residues.append(int(object[0]))
    par_rr_times.append(float(object[1]))

par_hc_results = par_hc_results[2:]
par_hc_residues = []
par_hc_times = []
for i in range(len(par_hc_results)):
    object = par_hc_results[i].split(",")
    par_hc_residues.append(int(object[0]))
    par_hc_times.append(float(object[1]))


par_sa_results = par_sa_results[2:]
par_sa_residues = []
par_sa_times = []
for i in range(len(par_sa_results)):
    object = par_sa_results[i].split(",")
    par_sa_residues.append(int(object[0]))
    par_sa_times.append(float(object[1]))

# No Prepartitioning
plt.plot(kk_residues, color='aqua',  label='KK Algorithm')
plt.plot(rr_residues, color='darkseagreen',
         label='Repeated Random Algorithm')
plt.plot(hc_residues, color='firebrick',
         label='Hill Climbing Algorithm')
plt.plot(sa_residues, color='darkkhaki',
         label='Simulated Annealing Algorithm')

plt.legend()
plt.xlabel('Instance')
plt.ylabel('Residue')
plt.title(
    'Comparison of Algorithms on the Number Partition Problem(No Prepartitioning)')

plt.show()

# Prepartitioning
plt.plot(kk_residues, color='aqua',  label='KK Algorithm')
plt.plot(par_rr_residues, color='darkseagreen',
         label='Repeated Random Algorithm')
plt.plot(par_hc_residues, color='firebrick',
         label='Hill Climbing Algorithm')
plt.plot(par_sa_residues, color='darkkhaki',
         label='Simulated Annealing Algorithm')

plt.legend()
plt.xlabel('Instance')
plt.ylabel('Residue')
plt.title(
    'Comparison of Algorithms on the Number Partition Problem(Prepartitioning)')

plt.show()


# Ignoring KK Algorithm
plt.plot(par_rr_residues, color='darkseagreen',
         label='Repeated Random Algorithm')
plt.plot(par_hc_residues, color='firebrick',
         label='Hill Climbing Algorithm')
plt.plot(par_sa_residues, color='darkkhaki',
         label='Simulated Annealing Algorithm')

plt.legend()
plt.xlabel('Instance')
plt.ylabel('Residue')
plt.title(
    'Comparison of Algorithms on the Number Partition Problem(Prepartitioning)')

plt.show()

# No Prepartitioning
plt.plot(kk_times, color='aqua',  label='KK Algorithm')
plt.plot(rr_times, color='darkseagreen',
         label='Repeated Random Algorithm')
plt.plot(hc_times, color='firebrick',
         label='Hill Climbing Algorithm')
plt.plot(sa_times, color='darkkhaki',
         label='Simulated Annealing Algorithm')

plt.legend()
plt.xlabel('Instance')
plt.ylabel('Time')
plt.title(
    'Comparison of Algorithm Times on the Number Partition Problem(No Prepartitioning)')

plt.show()

# Prepartitioning
plt.plot(kk_times, color='aqua',  label='KK Algorithm')
plt.plot(par_rr_times, color='darkseagreen',
         label='Repeated Random Algorithm')
plt.plot(par_hc_times, color='firebrick',
         label='Hill Climbing Algorithm')
plt.plot(par_sa_times, color='darkkhaki',
         label='Simulated Annealing Algorithm')

plt.legend()
plt.xlabel('Instance')
plt.ylabel('Time')
plt.title(
    'Comparison of Algorithm Times on the Number Partition Problem(Prepartitioning)')

plt.show()


# Averages

print(statistics.mean(kk_residues))
print(statistics.mean(kk_times))
print(statistics.mean(rr_residues))
print(statistics.mean(rr_times))
print(statistics.mean(hc_residues))
print(statistics.mean(hc_times))
print(statistics.mean(sa_residues))
print(statistics.mean(sa_times))
print(statistics.mean(par_rr_residues))
print(statistics.mean(par_rr_times))
print(statistics.mean(par_hc_residues))
print(statistics.mean(par_hc_times))
print(statistics.mean(par_sa_residues))
print(statistics.mean(par_sa_times))
