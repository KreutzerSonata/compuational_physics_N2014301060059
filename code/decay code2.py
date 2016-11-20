class uranium_decay:
    def __init__(self, number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.n_uranium_A = [number_of_nuclei_A]
        self.n_uranium_B = [number_of_nuclei_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
def calculate(self):
        for i in range(self.nsteps):
            tmpA = self.n_uranium_A[i] + (self.n_uranium_B[i] / self.tau -self.n_uranium_A[i] / self.tau)* self.dt
            tmpB = self.n_uranium_B[i] + (self.n_uranium_A[i] / self.tau -self.n_uranium_B[i] / self.tau)* self.dt
            self.n_uranium_A.append(tmpA)
            self.n_uranium_B.append(tmpB)
            self.t.append(self.t[i] + self.dt)
from math import *
class exact_results_check(uranium_decay):
    def show_results(self):
        self.etA = []
        self.etA = []
        for i in range(len(self.t)):
            tempA = self.n_uranium[0]*0.5 - self.n_uranium(0)*exp(-2*self.t[i] / self.tau)*0.5 + 2*self.n_uranium_A(0)*exp(-2*self.t[i] / self.tau)*0.5
            tempB = self.n_uranium[0]*0.5 + self.n_uranium(0)*exp(-2*self.t[i] / self.tau)*0.5 - 2*self.n_uranium_A(0)*exp(-2*self.t[i] / self.tau)*0.5
            self.etA.append(tempA)
            self.etB.append(tempB)
        plot1, = pl.plot(self.t, self.etA, 'r')
        plot2, = pl.plot(self.t, self.etB, 'g')
        plot3, = pl.plot(self.t, self.n_uranium_A, '*')
        plot4, = pl.plot(self.t, self.n_uranium_B, '*')
        pl.xlabel('time($s$)')
        pl.ylabel('Number of Nuclei')
        first_legend = pl.legend([plot1,plot2,plot3,plot4],['A','B','etA','etB'],loc='best')
        pl.xlim(0, self.time)
        pl.show()
a = exact_results_check(number_of_nuclei_A = 100, number_of_nuclei_B =0, time_constant = 1, time_of_duration = 5, time_step=0.05)
a.calculate()
a.show_results
