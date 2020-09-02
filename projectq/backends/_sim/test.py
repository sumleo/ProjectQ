import time
import projectq.backends._sim._pysim as pysim

loop = 25
begin = time.time()
sim = pysim.Simulator(1)
for i in range(loop):
    sim.allocate_qubit(i)
print(f'{loop},  {time.time() - begin}')
