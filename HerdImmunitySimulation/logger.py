class Logger:
    def __init__(self, filename):
        self.file = open(filename, 'w')

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):
        self.file.write(f"Population Size: {pop_size}\n")
        self.file.write(f"Vaccination Percentage: {vacc_percentage}\n")
        self.file.write(f"Virus Name: {virus_name}\n")
        self.file.write(f"Mortality Rate: {mortality_rate}\n")
        self.file.write(f"Reproduction Rate: {repro_rate}\n")
        self.file.write('\n')

    def log_interaction(self, person1, person2, did_infect=None, person2_vacc=None, person2_sick=None):
        interaction = f"Person {person1._id} interacted with Person {person2._id}"
        if did_infect:
            interaction += f" and infected them.\n"
        elif person2_vacc:
            interaction += f" but they were vaccinated.\n"
        elif person2_sick:
            interaction += f" but they were already infected.\n"
        else:
            interaction += f" with no infection.\n"
        self.file.write(interaction)

    def log_infection_survival(self, person, did_die_from_infection):
        if did_die_from_infection:
            self.file.write(f"Person {person._id} died from the infection.\n")
        else:
            self.file.write(f"Person {person._id} survived the infection.\n")

    def log_time_step(self, time_step_number):
        self.file.write(f"\nTime step {time_step_number} ended.\n")
        self.file.write("=====================\n")

    def close(self):
        self.file.close()
