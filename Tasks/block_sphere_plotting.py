"""
Created on August 2nd, 2019
@author: hossein.mohebbi
"""

import numpy as np
from scipy.linalg import expm # matrix exponential function
import warnings
warnings.filterwarnings('ignore')


class SphereVal:
    def __init__(self, k, w, rabi_freq, csv_data):
        self.k = k
        self.w = w*(10**6)
        self.rabi_freq = rabi_freq*(10**6)
        self.csv_data = csv_data
        self.csv_data_length = len(csv_data)

        # Pauli Spin Matrices
        self.s_x = np.matrix([[0, 1], [1, 0]])
        self.s_y = np.matrix([[0, -1j], [1j, 0]])
        self.s_z = np.matrix([[1, 0], [0, -1]])

    def hamiltonian(self, w, amplitude, phase, k):
        # the equation
        return 0.5*2*np.pi*w*self.s_z +\
               0.5*2*np.pi*amplitude*k*self.rabi_freq*\
               (np.cos(np.radians(phase))*self.s_x + np.sin(np.radians(phase))*self.s_y)

    # function that returns expectation values against k_range
    def sigmas(self):
        sigma_x_expecs = []
        sigma_y_expecs = []
        sigma_z_expecs = []

        total_time = 0
        csv_time = [0]
        csv_amplitude = []
        csv_phase = []
        for i in range(self.csv_data_length):
            csv_amplitude.append(float(self.csv_data[i][1]))
            csv_phase.append(float(self.csv_data[i][2]))
            csv_time.append(float(self.csv_data[i][0]) + csv_time[i]) # remember this is still in seconds
            total_time += float(self.csv_data[i][0]) # remember this is still in seconds

        del csv_time[0] # must delete initial 0
        time = []
        amplitude = []
        phase = []
        counter = 0
        for i in range(int(total_time)):
            if i > csv_time[counter]:
                counter += 1
            amplitude.append(csv_amplitude[counter])
            phase.append(csv_phase[counter])
            time.append(i * (10 ** (-9))) # converted to nanoseconds now

        times_len = len(time)
        P = self.s_z
        for i in range(times_len):
            a = amplitude[i]
            p = phase[i]
            H = self.hamiltonian(self.w, a, p, self.k)
            U = expm((10 ** (-9)) * (-1j) * H) # 1 ns stepping
            U_H = np.conj(U).T
            P = np.dot(U, np.dot(P, U_H))  # begins with p0=self.s_z then grows each iteration

            # calculate traces to get expec vals
            expec_x = 0.5 * np.trace(P * self.s_x)
            expec_y = 0.5 * np.trace(P * self.s_y)
            expec_z = 0.5 * np.trace(P * self.s_z)

            sigma_x_expecs.append(float(expec_x))
            sigma_y_expecs.append(float(expec_y))
            sigma_z_expecs.append(float(expec_z))

        return sigma_x_expecs, sigma_y_expecs, sigma_z_expecs


'''TEST'''
'''
x = SphereVal(5, 2, 1, [[333.3,2.1,0],[250,1,0],[210,5,0],[222,1,1]])
s = x.sigmas()
print s[0]
print s[1]
print s[2]
'''
