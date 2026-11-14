# twin spool high bypass turbofan
#assumptions = Cp, Cv constant, compression and expansion processes are isentropic, mass flow constant
import numpy as np
#constants
C_p=1.005*10**3 #J*K/kg
C_v=0.718*10**3#J*K/kg
gamma=1.4

#conditions
p_amb=10e5 #pa
T_amb=273.15 #K

#Input
Cruise_speed=0.83 #M
Bypass_ratio=8

#pressure ratios
LPC_pr= 3.5
HPC_pr= 5



combustor_pr=0.97 


combustor_exit_temp=1400 #K


#isentrop efficiencies
i_inlet=0.97
i_fan=0.98
i_LPC=0.95
i_HPC=0.94
i_LPT=0.9
i_HPT=0.85




#calculations

