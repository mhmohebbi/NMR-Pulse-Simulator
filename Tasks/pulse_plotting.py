"""
Created on August 8th, 2019
@author: hossein.mohebbi
"""

import numpy as np


class Pulse:
    def __init__(self, csv_data):
        self.csv_data = csv_data
        self.length = len(csv_data)

    def get_pulse_arrays(self):
        amplitude = []
        phase = []
        time_ns = []
        time_counter = 0
        time_ns.append(time_counter)
        amplitude.append(0)
        phase.append(0)
        time_counter += 100
        time_ns.append(time_counter)
        amplitude.append(0)
        phase.append(0)
        # goes through data appending correct times and amplitudes/phases, 100ns space begin and end
        for i in range(self.length):

            time_ns.append(time_counter)
            amplitude.append(float(self.csv_data[i][1]))
            phase.append(float(self.csv_data[i][2]))
            time_counter += float(self.csv_data[i][0])
            time_ns.append(time_counter)
            amplitude.append(float(self.csv_data[i][1]))
            phase.append(float(self.csv_data[i][2]))

        amplitude.append(0)
        phase.append(0)
        time_ns.append(time_counter)
        time_counter += 100
        time_ns.append(time_counter)
        amplitude.append(0)
        phase.append(0)

        # components for polar form
        x_comp = []
        y_comp = []
        length = len(phase)
        for i in range(length):
            x_comp.append(amplitude[i] * np.cos(np.radians(phase[i])))
            y_comp.append(amplitude[i] * np.sin(np.radians(phase[i])))

        return time_ns, amplitude, phase, x_comp, y_comp











