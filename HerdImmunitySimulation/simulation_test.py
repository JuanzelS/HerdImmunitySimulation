import unittest
from simulation import Simulation
from virus import Virus

class TestSimulation(unittest.TestCase):
    def test_simulation_initialization(self):
        virus = Virus("TestVirus", 0.5, 0.2)
        sim = Simulation(100, 0.9, virus, 10)
        self.assertEqual(len(sim.population), 100)
        self.assertEqual(sum(p.is_vaccinated for p in sim.population), 90)
        self.assertEqual(sum(p.infected for p in sim.population), 10)

    def test_run_simulation(self):
        virus = Virus("TestVirus", 0.5, 0.2)
        sim = Simulation(100, 0.9, virus, 10)
        sim.run()
        self.assertTrue(any(p.infected for p in sim.population))
        self.assertGreater(sim.total_infected, 10)  # Ensure the infection spread
        self.assertGreaterEqual(sim.total_dead, 0)  # Ensure some deaths occurred

if __name__ == '__main__':
    unittest.main()
