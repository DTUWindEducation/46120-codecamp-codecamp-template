"""Turbie functions.
"""
import numpy as np

def load_resp(path_resp,t_start=0):
    data = np.loadtxt(path_resp,skiprows=1)
    time_column = data[:,0] # Get the time column
    start_index = np.where(time_column >= t_start)[0][0]  # Get first occurrence
    data_filter = data[start_index:,:]
    t = data_filter[:,0]
    u = data_filter[:,1]
    xb = data_filter[:,2]
    xt = data_filter[:,3]
    return [t,u,xb,xt]

def load_wind(path_wind,t_start=0):
    data = np.loadtxt(path_wind,skiprows=1)
    time_column = data[:,0] # Get the time column
    start_index = np.where(time_column >= t_start)[0][0]  # Get first occurrence
    data_filter = data[start_index:,:]
    t_wind = data_filter[:,0]
    u_wind = data_filter[:,1]
    return [t_wind,u_wind]