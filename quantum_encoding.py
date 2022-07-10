# Following this course: https://learn.qiskit.org/course/introduction/the-atoms-of-computation
from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
qc = QuantumCircuit(3,3)
qc.measure([0,1,2], [0,1,2])
qc.draw()

simulator = AerSimulator()

job = simulator.run(qc)
result = job.result()
result.get_counts()

# "By convention, qubits always start in the state 0"

## More complicated version with an x-gate -- NOT or flipping the bit value

qc2 = QuantumCircuit(3,3)
qc2.x([0,1])
qc2.measure([0,1,2], [0,1,2])
qc2.draw()

job2 = simulator.run(qc2)
result2 = job2.result()
result2.get_counts()

## Note seems that [2] is the third order, so for [0,1,2] the encoded string is f"[2][1][0]"

# Test: encoding the number four to binary (4 -> 100)

qc3 = QuantumCircuit(3,3)
qc3.x([2])
qc3.measure([0,1,2], [0,1,2])
qc3.draw()

job3 = simulator.run(qc3)
result3 = job3.result()
result3.get_counts()

# For 6 -> 110

qc4 = QuantumCircuit(3,3)
qc4.x([2,3])
qc4.measure([0,1,2], [0,1,2])
qc4.draw()

job4 = simulator.run(qc4)
result4 = job4.result()
result4.get_counts()
