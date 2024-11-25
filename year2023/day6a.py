""" Solution for 6a """
from aocd import get_data

def main():
    """Main function for 6a"""
    data = get_data(day=6, year=2023).split("\n")
    times = list(map(int, data[0].split(":")[1].split()))
    distances = list(map(int, data[1].split(":")[1].split()))
    wins = []
    for race_num, time in enumerate(times):
        race = []
        speed = time
        for i in range(time):
            if (i * (speed)) > distances[race_num]:
                race.append(i)
            speed -= 1
        wins.append(race)

    answer = len(wins[0]*len(wins[1])*len(wins[2])*len(wins[3]))
    print(answer)

if __name__ == "__main__":
    main()
