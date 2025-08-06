import scipy as sp
import scipy.signal
import scipy.fftpack
import matplotlib.pyplot as plt
import numpy as np

class Iinp_FFT:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            #print(key,value)
            setattr(self,key,value)
        self.cycles=4
        self.datapoints=np.linspace(0,1.024,1024)
        self.time_datapoints=self.datapoints/self.Fs*self.cycles

        self.i_zin_ac  = self.create_i_zin_waveform()
        self.i_zin_fft = sp.fftpack.fft(self.i_zin_ac[:512])
        self.freq      = sp.fftpack.fftfreq(self.i_zin_fft.size,self.time_datapoints[1])
                                             
    def create_i_zin_waveform(self):
        duty = self.Vout/self.Vin; ipp = (self.Vin-self.Vout)*duty/self.Fs/self.Lout
        Iin_avg = self.Vout*self.Iout/self.Vin
        I_inductor=sp.signal.sawtooth(2*np.pi*self.datapoints*self.cycles,duty)/2*ipp+self.Iout
        dfactor = {'2level':1,'3level':2}[self.Level]
        D_pulse = sp.signal.square(2*np.pi*self.datapoints*self.cycles/dfactor,duty/dfactor)/2+.5
        I_HSfet = D_pulse*I_inductor
        return I_HSfet - Iin_avg

    def plot_i_zin_fft(self):
        i_zin_fft_mag = np.abs(self.i_zin_fft)
        ampscale=2/self.i_zin_fft.size
        xticks = np.arange(8)*self.Fs
        i=self.freq>=0
        bar_width=300000
        fig,ax = plt.subplots(1,1,figsize=(8,4))
        rects1=ax.bar(self.freq[i],ampscale*i_zin_fft_mag[i],bar_width)
        ax.set_xlim(0,8*self.Fs)
        ax.set_xticks(xticks)
        plt.show()


        