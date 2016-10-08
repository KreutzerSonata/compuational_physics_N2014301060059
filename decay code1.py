import pylab as pl
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
    def show_results(self):
        plot1, = pl.plot(self.t, self.n_uranium_A)
        plot2, = pl.plot(self.t, self.n_uranium_B)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        first_legend = pl.legend([plot1,plot2],['Number of Nuclei A','Number of Nuclei B'],loc = 'best')
        pl.show()
a = uranium_decay()
a.calculate()
a.show_results()
