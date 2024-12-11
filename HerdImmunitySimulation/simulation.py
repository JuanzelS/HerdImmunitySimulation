import random
from person import Person
from virus import Virus
from logger import Logger

class Simulation:
    def __init__(self, population_size, vacc_percentage, virus, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.virus = virus
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.logger = Logger('simulation.log')
        self.total_infected = initial_infected
        self.total_dead = 0

        self.logger.write_metadata(population_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)

    def _create_population(self):
        population = []
        num_vaccinated = int(self.population_size * self.vacc_percentage)
        num_infected = self.initial_infected

        for i in range(self.population_size):
            if i < num_vaccinated:
                person = Person(i, True)
            elif i < num_vaccinated + num_infected:
                person = Person(i, False, True)
            else:
                person = Person(i, False)
            population.append(person)
        return population

    def _simulation_should_continue(self):
        for person in self.population:
            if person.infected and person.is_alive:
                return True
        return False

    def time_step(self, time_step_number):
        newly_infected = []

        for person in self.population:
            if person.infected and person.is_alive:
                for _ in range(100):
                    random_person = random.choice(self.population)
                    if random_person.is_alive and not random_person.is_vaccinated and not random_person.infected:
                        if random.random() < self.virus.repro_rate:
                            newly_infected.append(random_person)
                            self.logger.log_interaction(person, random_person, did_infect=True)
                        else:
                            self.logger.log_interaction(person, random_person, did_infect=False)
                    else:
                        if random_person.is_vaccinated:
                            self.logger.log_interaction(person, random_person, person2_vacc=True)
                        if random_person.infected:
                            self.logger.log_interaction(person, random_person, person2_sick=True)

        for person in newly_infected:
            person.infected = True
            self.total_infected += 1

        for person in self.population:
            if person.infected:
                if not person.did_survive_infection(self.virus.mortality_rate):
                    self.total_dead += 1
                    self.logger.log_infection_survival(person, did_die_from_infection=True)
                else:
                    self.logger.log_infection_survival(person, did_die_from_infection=False)

        self.logger.log_time_step(time_step_number)

    def run(self):
        time_step_counter = 0
        while self._simulation_should_continue():
            print(f"Running time step {time_step_counter}")
            self.time_step(time_step_counter)
            time_step_counter += 1
        print(f'The simulation has ended after {time_step_counter} turns. Total infected: {self.total_infected}, Total dead: {self.total_dead}')
