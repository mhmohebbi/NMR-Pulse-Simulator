"""
Created on August 16th, 2019
@author: hossein.mohebbi
"""

import threading
import numpy as np
from scipy.linalg import expm # matrix exponential function
import warnings
warnings.filterwarnings('ignore')


class ContourPlotExpectVal(threading.Thread):
    def __init__(self, k_range, w_range, rabi_freq, csv_data):
        threading.Thread.__init__(self)
        self.counter = 0
        self.k_range = k_range
        self.w_range = w_range
        self.rabi_freq = rabi_freq*(10**6)
        self.csv_data = csv_data
        self.csv_data_length = len(csv_data)
        self.w_range_len = len(w_range)
        self.k_range_len = len(k_range)
        self.progress = 0
        self.matrix_dic = {}

        # termination
        self._stop = threading.Event()
        self.progress_complete = False

        # Pauli Spin Matrices
        self.s_x = np.matrix([[0, 1], [1, 0]])
        self.s_y = np.matrix([[0, -1j], [1j, 0]])
        self.s_z = np.matrix([[1, 0], [0, -1]])

    def hamiltonian(self, w, amplitude, phase, k):
        self.counter += 1
        if self.progress > 98:
            self.progress = 99
        else:
            self.progress = 100 * self.counter / (self.w_range_len * self.k_range_len * self.csv_data_length * 6)

        # the equation
        return 0.5*2*np.pi*w*self.s_z +\
               0.5*2*np.pi*amplitude*k*self.rabi_freq*\
               (np.cos(np.radians(phase))*self.s_x + np.sin(np.radians(phase))*self.s_y)

    def sigma(self, k, w):
        p0 = self.s_z

        # first loop multiplies all U daggers (U1 to Ui)
        U_H = 1
        for i in range(self.csv_data_length):
            time = float(self.csv_data[i][0]) * (10 ** (-9))
            amplitude = float(self.csv_data[i][1])
            phase = float(self.csv_data[i][2])
            H = self.hamiltonian(w, amplitude, phase, k)
            U = expm(time * (-1j) * H)
            U_H *= np.conj(U).T

        # second loop multiplies all U (Ui to U1)
        U = 1
        for i in reversed(range(self.csv_data_length)):
            time = float(self.csv_data[i][0]) * (10 ** (-9))
            amplitude = float(self.csv_data[i][1])
            phase = float(self.csv_data[i][2])
            H = self.hamiltonian(w, amplitude, phase, k)
            U *= expm(time * (-1j) * H)

        # calculate correct roe (P) value
        P = U * p0 * U_H

        # calculate traces to get expec vals
        expec_x = 0.5 * np.trace(P * self.s_x)
        expec_y = 0.5 * np.trace(P * self.s_y)
        expec_z = 0.5 * np.trace(P * self.s_z)

        return float(expec_x), float(expec_y), float(expec_z)

    def run(self):
        print "started compilation thread"
        # k always x
        # w always y
        z_sigma_x = []
        z_sigma_y = []
        z_sigma_z = []
        for i in range(self.k_range_len):
            row_x = []
            row_y = []
            row_z = []
            for j in range(self.w_range_len):
                row_x.append(self.sigma(self.k_range[i], self.w_range[j])[0])
                row_y.append(self.sigma(self.k_range[i], self.w_range[j])[1])
                row_z.append(self.sigma(self.k_range[i], self.w_range[j])[2])
            z_sigma_x.append(row_x)
            z_sigma_y.append(row_y)
            z_sigma_z.append(row_z)

        self.matrix_dic = {
            "z_sigma_x": z_sigma_x,
            "z_sigma_y": z_sigma_y,
            "z_sigma_z": z_sigma_z
        }

        self.progress_complete = True
        print "DONE"

    def shutdown(self):
        self._stop.set()
        print "shutting thread"

    def is_shutdown(self):
        return self._stop.is_set()

'''TEST'''
"""
q = GlPlotExpectVal([1, 2, 3], [500000, 500001, 500002], 10, [[250, 1, 0]])
print q.run()
"""
