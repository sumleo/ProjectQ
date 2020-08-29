#   Copyright 2017 ProjectQ-Framework (www.projectq.ch)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Tests for projectq.backends._sim._simulator.py, using both the Python
and the C++ simulator as backends.
"""

import copy
import math
import numpy
import pytest
import random
import scipy
import scipy.sparse
import scipy.sparse.linalg

from projectq import MainEngine
from projectq.cengines import (BasicEngine, BasicMapperEngine, DummyEngine,
                               LocalOptimizer, NotYetMeasuredError)
from projectq.ops import (All, Allocate, BasicGate, BasicMathGate, CNOT,
                          Command, H, MatrixGate, Measure, QubitOperator,
                          Rx, Ry, Rz, S, TimeEvolution, Toffoli, X, Y, Z)
from projectq.meta import Control, Dagger, LogicalQubitIDTag
from projectq.types import WeakQubitRef

# from projectq.backends import Simulator
from projectq.backends._sim._simulator import FALLBACK_TO_PYSIM
from projectq.backends._sim._simulator import Simulator


def test_simulator_functional_measurement(sim):
    eng = MainEngine(sim, [])
    qubits = eng.allocate_qureg(5)
    # entangle all qubits:
    H | qubits[0]
    for qb in qubits[1:]:
        CNOT | (qubits[0], qb)

    All(Measure) | qubits

    bit_value_sum = sum([int(qubit) for qubit in qubits])
    assert bit_value_sum == 0 or bit_value_sum == 5


if __name__ == '__main__':
    print("FALLBACK_TO_PYSIM", FALLBACK_TO_PYSIM)
    test_simulator_functional_measurement(Simulator())
