from sensorbeacon import SensorBeaconMap, SensorBeaconPair
from utils import read_input, read_example
from pathlib import Path


run = "input"

ys = {"input": 2000000, "example": 10}
maxDists = {"input": 4000000, "example": 20}


def convert_input(lines: list) -> SensorBeaconMap:
    separators = ["Sensor at x=",  ", y=", ": closest beacon is at x="]
    sensor_beacon_map = SensorBeaconMap()
    for line in lines:
        for separator in separators:
            line = line.replace(separator, ",")
        values = [int(s) for s in line.split(",")[1:]]
        sensor_position = tuple(values[:2])
        beacon_position = tuple(values[2:])
        sensor_beacon_map.add_pair(SensorBeaconPair(sensor_position=sensor_position, beacon_position=beacon_position))
    return sensor_beacon_map


def solve1() -> str:
    file_dir = Path(__file__).parent
    if run == "input":
        sensor_beacon_map = convert_input(lines=read_input(file_dir=file_dir))
    elif run == "example":
        sensor_beacon_map = convert_input(lines=read_example(file_dir=file_dir))
    else:
        raise Exception("either choose input or example to run")
    result = sensor_beacon_map.impossible_positions_in_line(y=ys[run])
    return f"In the line with y={ys[run]} are {len(result)} positions that cannot contain a beacon"


def solve2() -> str:
    pass


def main():
    print(solve1())
    print(solve2())


if __name__ == "__main__":
    main()

