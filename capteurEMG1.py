


class EMGsensor:

    def generate_emg_data(self):
        return 100
    
    def read_emg(self):
        emg_data = self.generate_emg_data()
        for i in range(10):
            emg_data += 5*i
            yield emg_data


def main():
    sensor1 = EMGsensor()
    for emg_data in sensor.read_emg():
        print("moteur bouge de ", emg_data)




