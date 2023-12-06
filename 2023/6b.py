""" Solution for 6b """
from aocd import get_data

def main():
    """Main function for 6b"""
    data = get_data(day=6, year=2023).split("\n")
    time = int("".join(data[0].split(":")[1].split()))
    distance = int("".join(data[1].split(":")[1].split()))
    wins = 0
    speed = time
    for i in range(time):
        if (i * (speed)) > distance:
            wins += 1
        speed -= 1
    print(wins)

if __name__ == "__main__":
    main()
