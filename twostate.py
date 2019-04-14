# coding: utf-8

class Two_state:
    
    def __init__(self,t1,t2):
        self.t1 = t1
        self.t2 = t2
        self.Ts = t1+t2
    
# unit step function (in mathcad, was in kronicker delta section)
    def step(self,t):
        if t<0:
            kd=0
        elif t==0:
            kd=0.5
        else:
            kd=1
        return kd
            
# unit pulse functions have 'time' integer input and output a 1, 0 or 0.5
    def t1_unit_pulse(self,t):
        return self.step(self.t1-t)
    
    def t2_unit_pulse(self,t):
        return (1-self.t1_unit_pulse(t))
    
    def repeating(self,t):
        period=self.Ts
        return (t-(t//period)*period)

# pulse train functions have 'time' max input and output an array of 1's, 0's and 0.5's
    def t1_pulse_train(self,tmax):
        pulsetrain=[]
        for t_idx in range(tmax):
            pulsetrain.append(self.t1_unit_pulse(self.repeating(t_idx)))
        return pulsetrain
    
    def t2_pulse_train(self,tmax):
        pulsetrain=[]
        for t_idx in range(tmax):
            pulsetrain.append(self.t2_unit_pulse(self.repeating(t_idx)))
        return pulsetrain

