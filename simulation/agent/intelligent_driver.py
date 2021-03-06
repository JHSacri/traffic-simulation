import math
from simulation.agent.driver import Driver
from simulation.simulation_object import SimulationObject


class IntelligentDriver(Driver):

    def __init__(self, min_spacing: float =12.0, time_headway: float =1.0, comf_break: float =3.0, delta: float=4.0,
                 politeness: float =0.5, b_safe: float =3.0, thresh: float =0.4):
        super(IntelligentDriver, self).__init__(politeness, b_safe, thresh)
        # IDM parameters (v_0 and a_max are implemented as agent parameters)
        self.min_spacing = min_spacing
        self.time_headway = time_headway
        self.comf_break = comf_break
        self.delta = delta

    def decide_acceleration(self, ego: SimulationObject, front: SimulationObject,
                            bumper_distance: float, v_delta: float):
        if front is None:
            return ego.max_acceleration
        if bumper_distance <= 0:
            return -float('inf')

        s_star = self.min_spacing + ego.velocity * self.time_headway + (ego.velocity * v_delta / (2 * math.sqrt(ego.max_acceleration * self.comf_break)))
        acceleration = ego.max_acceleration * (1 - (ego.velocity / ego.max_velocity)**self.delta - (s_star / bumper_distance)**2)

        return acceleration
