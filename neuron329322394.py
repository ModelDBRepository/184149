'''
Defines a class, Neuron329322394, of neurons from Allen Brain Institute's model 329322394

A demo is available by running:

    python -i mosinit.py
'''
class Neuron329322394:
    def __init__(self, name="Neuron329322394", x=0, y=0, z=0):
        '''Instantiate Neuron329322394.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron329322394_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Nr5a1-Cre_Ai14_IVSCC_-169248.04.02.01_403165543_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron329322394_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 69.61
            sec.e_pas = -87.0689697266
        for sec in self.apic:
            sec.cm = 3.33
            sec.g_pas = 0.000130161924261
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000942829369333
        for sec in self.dend:
            sec.cm = 3.33
            sec.g_pas = 2.1198350623e-05
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 3.05131e-05
            sec.gbar_Ih = 0.00600216
            sec.gbar_NaTs = 0.86381
            sec.gbar_Nap = 0.00164837
            sec.gbar_K_P = 0.00130214
            sec.gbar_K_T = 0.00934683
            sec.gbar_SK = 0.00392186
            sec.gbar_Kv3_1 = 0.266399
            sec.gbar_Ca_HVA = 0.000616792
            sec.gbar_Ca_LVA = 0.00398975
            sec.gamma_CaDynamics = 0.000405505
            sec.decay_CaDynamics = 897.721
            sec.g_pas = 0.000580353
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

