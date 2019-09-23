"""
Created on August 2nd, 2019
@author: hossein.mohebbi
"""

import numpy as np
from scipy.linalg import expm # matrix exponential function
import warnings
warnings.filterwarnings('ignore')


class ExpectVal:
    def __init__(self, k_range, k_step, w_range, w_step, rabi_freq, csv_data):
        self.k_range = []
        self.k_step = k_step
        self.w_range = []
        self.w_step = w_step*(10**3)
        self.rabi_freq = rabi_freq*(10**6)
        self.csv_data = csv_data
        self.csv_data_length = len(csv_data)

        # Pauli Spin Matrices
        self.s_x = np.matrix([[0, 1], [1, 0]])
        self.s_y = np.matrix([[0, -1j], [1j, 0]])
        self.s_z = np.matrix([[1, 0], [0, -1]])

        # determining k range to be looping through
        k_range_vals = k_range[0]
        k_range_threshold = k_range[1]
        while k_range_vals <= k_range_threshold:
            self.k_range.append(k_range_vals)
            k_range_vals += self.k_step

        # determining w range to be looping through
        w_range_vals = w_range[0]*(10**6)
        w_range_threshold = w_range[1]*(10**6)
        while w_range_vals <= w_range_threshold:
            self.w_range.append(w_range_vals)
            w_range_vals += self.w_step

    def hamiltonian(self, w, amplitude, phase, k):
        # the equation
        return 0.5*2*np.pi*w*self.s_z +\
               0.5*2*np.pi*amplitude*k*self.rabi_freq*\
               (np.cos(np.radians(phase))*self.s_x + np.sin(np.radians(phase))*self.s_y)

    # function that returns expectation values against k_range
    def sigma_k(self):
        p0 = self.s_z
        sigma_x_expecs = []
        sigma_y_expecs = []
        sigma_z_expecs = []

        for k in self.k_range:
            # first loop multiplies all U daggers (U1 to Ui)
            U_H = [[1, 0],
                   [0, 1]]
            for i in range(self.csv_data_length):
                time = float(self.csv_data[i][0]) * (10 ** (-9))
                amplitude = float(self.csv_data[i][1])
                phase = float(self.csv_data[i][2])
                # self.w_range[0] ends up being user selected value for w
                H = self. hamiltonian(self.w_range[0], amplitude, phase, k)
                U = expm(time*(+1j)*H)
                U_H = np.dot(U_H, np.conj(U).T)

            # second loop multiplies all U (Ui to U1)
            U = [[1, 0],
                 [0, 1]]
            for i in reversed(range(self.csv_data_length)):
                time = float(self.csv_data[i][0]) * (10 ** (-9))
                amplitude = float(self.csv_data[i][1])
                phase = float(self.csv_data[i][2])
                # self.w_range[0] ends up being user selected value for w
                H = self. hamiltonian(self.w_range[0], amplitude, phase, k)
                U = np.dot(U, expm(time*(-1j)*H))

            # calculate correct roe (P) value for each w in w_range
            P = np.dot(U, np.dot(p0, U_H))

            # calculate traces to get expec vals
            expec_x = 0.5 * np.trace(P * self.s_x)
            expec_y = 0.5 * np.trace(P * self.s_y)
            expec_z = 0.5 * np.trace(P * self.s_z)

            sigma_x_expecs.append(float(expec_x))
            sigma_y_expecs.append(float(expec_y))
            sigma_z_expecs.append(float(expec_z))

        return sigma_x_expecs, sigma_y_expecs, sigma_z_expecs

    # function that returns expectation values against w_range
    def sigma_w(self):
        p0 = self.s_z
        sigma_x_expecs = []
        sigma_y_expecs = []
        sigma_z_expecs = []

        for w in self.w_range:
            # first loop multiplies all U daggers (U1 to Ui)
            U_H = [[1, 0],
                   [0, 1]]
            for i in range(self.csv_data_length):
                time = float(self.csv_data[i][0]) * (10 ** (-9))
                amplitude = float(self.csv_data[i][1])
                phase = float(self.csv_data[i][2])
                # self.k_range[0] ends up being user selected value for k
                H = self. hamiltonian(w, amplitude, phase, self.k_range[0])
                U = expm(time*(-1j)*H)
                U_H = np.dot(U_H, np.conj(U).T)

            # second loop multiplies all U (Ui to U1)
            U = [[1, 0],
                 [0, 1]]
            for i in reversed(range(self.csv_data_length)):
                time = float(self.csv_data[i][0]) * (10 ** (-9))
                amplitude = float(self.csv_data[i][1])
                phase = float(self.csv_data[i][2])
                # self.k_range[0] ends up being user selected value for k
                H = self. hamiltonian(w, amplitude, phase, self.k_range[0])
                U = np.dot(U, expm(time*(-1j)*H))

            # calculate correct roe (P) value for each w in w_range
            P = np.dot(U, np.dot(p0, U_H))

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
x = ExpectVal((-5,5),100, 1, [[333,2.1,0],[250,1,0],[210,5,0],[222,1,1]])
s = x.sigma()
print s[1] # y
'''
