#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:47:22 2025

@author: emefff
"""

import matplotlib.pyplot as plt
# importing pandas
import pandas as pd

# read text file into pandas DataFrame
df_force = pd.read_csv("/home/emefff/pythonProjects/OpenFOAM_auswerten/force.dat", sep=r'\s+', skiprows=3)
df_moment = pd.read_csv("/home/emefff/pythonProjects/OpenFOAM_auswerten/moment.dat", sep=r'\s+', skiprows=3)
# in python 3.12 '\s+' gives invalid escape sequence warning, thus r'\s+' necessary
    
print(f"{df_force.columns = }\n")
print(f"{df_moment.columns = }\n")

plt.figure(figsize=(15,9))
plt.plot(df_force['Time'], df_force['total_z'].abs(), 'k-', label='force_total_z')
plt.plot(df_moment['Time'], df_moment['total_z'].abs(), 'r-', label='moment_total_z')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()

# plt.figure(figsize=(15,9))
# plt.plot(df_force['Time'], df_force['total_x'].abs(), 'k-')
# plt.plot(df_force['Time'], df_force['total_y'].abs(), 'r-')
# plt.yscale('log')
# plt.show()

####################################################################
# read text file into pandas DataFrame
df_solver = pd.read_csv("/home/emefff/pythonProjects/OpenFOAM_auswerten/solverInfo.dat", sep=r'\s+', skiprows=1)
# in python 3.12 '\s+' gives invalid escape sequence warning, thus r'\s+' necessary
    
print(f"{df_solver.columns = }\n")

plt.figure(figsize=(15,9))
plt.plot(df_solver['Time'], df_solver['Uz_initial'].abs(), 'k-', label='Uz_initial')
plt.plot(df_solver['Time'], df_solver['Uz_final'].abs(), 'k--', label='Uz_final')
plt.plot(df_solver['Time'], df_solver['p_initial'].abs(), 'r-', label='p_initial')
plt.plot(df_solver['Time'], df_solver['p_final'].abs(), 'r--', label='p_final')
plt.plot(df_solver['Time'], df_solver['Uz_iters'].abs(), 'g-', label='Uz_iters')
plt.plot(df_solver['Time'], df_solver['p_iters'].abs(), 'g--', label='p_iters')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()
