def read_consumption(filename):
    try:
        with open(filename, "r") as file:
            lines = [line.strip().split(";") for line in file]
    except OSError:
        print("The file cannot be opened!")
    lines = lines[1:] #removing the first line containing indicators
    total_cons_dict = {} # forming a dict. Tkaing the ID as a key and then sum all the consumptions
    # for the day
    
    for line in lines:
        ID = line[0] 
        time = line[2]
        Energy_consumption = float(line[3])

        if line[0] not in total_cons_dict:
            total_cons_dict[ID] = Energy_consumption
        else:
            total_cons_dict[ID] += Energy_consumption
        
    return total_cons_dict

def read_system(filename):
    try:
        with open(filename, "r") as file:
            lines = [line.strip().split(";") for line in file]
            lines = lines[1:]
    except OSError:
        print("The file cannot be opened")
    system_dict = {}
    for line in lines:
        ID = line[0]
        system_size = float(line[1])
        system_efficiency = float(line[2])
        system_dict[ID] = [system_size,system_efficiency]
    
    return system_dict

def read_weather(filename):
    try:
        with open(filename, "r") as file:
            lines = [line.strip().split(";") for line in file]
            lines = lines[1:]
    except OSError:
        print("The file cannot be opened")
    weather_dict = {}
    for line in lines:
        time = line[1]
        solar_radiation = float(line[2])
        weather_dict[time] = solar_radiation

    return weather_dict
        
def Produce(system_dict,weather_dict):
    PEnergy_dict = {}
    for ID in system_dict:
        for time in weather_dict:
            if weather_dict[time] == 0:
                continue
            produced_energy = system_dict[ID][0] * system_dict[ID][1] * weather_dict[time]
            if ID not in PEnergy_dict:
                PEnergy_dict[ID] = produced_energy
            else:
                PEnergy_dict[ID] += produced_energy
    
    return PEnergy_dict

def energy_fed(PEnergy_dict,consumption_dict):
    
    Energy_dict = {}
    for ID in PEnergy_dict:
        energy_toGrid = PEnergy_dict[ID] - consumption_dict[ID]
        if energy_toGrid > 0:
            self_consumed_energy = consumption_dict[ID]
            Energy_dict[ID] = [energy_toGrid, self_consumed_energy]
        else:
            self_consumed_energy = PEnergy_dict[ID]
            Energy_dict[ID] = [0,self_consumed_energy]
    for ID in PEnergy_dict:
        self_consumption = (Energy_dict[ID][1]/ PEnergy_dict[ID]) * 100 #self consumed / total production) *100
        Energy_dict[ID].append(self_consumption)
    for ID in PEnergy_dict:
        self_sufficiency = (Energy_dict[ID][1]/consumption_dict[ID]) * 100
        Energy_dict[ID].append(self_sufficiency)
    #Energy_dict[ID] = {energy_toGrid, self_consumed_energy, self_consumption, self,sufficiency}
    
        
    
    return Energy_dict


def main():
    filename = "consumption.csv"
    consumption_dict = read_consumption(filename)
    filename = "systems.csv"
    system_dict = read_system(filename)
    filename = "weather.csv"
    weather_dict = read_weather(filename)
    Produced_energy_dict = Produce(system_dict,weather_dict)
    Energy_dict = energy_fed(Produced_energy_dict,consumption_dict)

    Produced_energy = 0
    Consumed_energy = 0
    Self_consumed_energy = 0
    Energy_togrid = 0
    Self_consumption = 0
    Self_sufficiency = 0
    
    for ID in Energy_dict:
        Produced_energy += Produced_energy_dict[ID]
        Consumed_energy += consumption_dict[ID]
        Self_consumed_energy += Energy_dict[ID][1]
        Energy_togrid += Energy_dict[ID][0]
        Self_consumption += Energy_dict[ID][2]
        Self_sufficiency += Energy_dict[ID][3]
    
    print("Aggregate report:")
    print("Produced Energy:", Produced_energy )
    print("Consumed Energy:", Consumed_energy)
    print("Self-consumed Energy:", Self_consumed_energy)
    print("Energy Fed into the Grid:", Energy_togrid)
    print("Self-consumption Percentage:", Self_consumption)
    print("Self-sufficiency Percentage:", Self_sufficiency)







main()