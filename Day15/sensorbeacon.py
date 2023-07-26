from typing import Tuple, Set
from tqdm import tqdm


def manhatten_distance(position1: Tuple[int, int], position2: Tuple[int, int]) -> int:
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def tuning_frequency(beacon_position: Tuple[int, int]) -> int:
    return 4000000 * beacon_position[0] + beacon_position[1]


class SensorBeaconPair:
    def __init__(self, sensor_position: tuple, beacon_position: tuple):
        self.sensor_position = sensor_position
        self.beacon_position = beacon_position
        self.manhatten_distance = manhatten_distance(sensor_position, beacon_position)
    
    def count_impossible_positions_in_line(self, y: int) -> int:
        y_distance_line_sensor = abs(self.sensor_position[1] - y)
        if y_distance_line_sensor > self.manhatten_distance:
            return 0
        else:
            return 1 + 2 * (self.manhatten_distance - y_distance_line_sensor)

    def impossible_positions_in_line(self, y: int) -> Set[Tuple[int, int]]:
        count = self.count_impossible_positions_in_line(y=y)
        offset = int((count - 1) / 2)
        return {(self.sensor_position[0] + o, y) for o in range(-1 * offset, offset + 1)}


class SensorBeaconMap:
    def __init__(self):
        self._pairs = []

    def __len__(self):
        return len(self._pairs)

    def __getitem__(self, item) -> SensorBeaconPair:
        return self._pairs[item]

    def __iter__(self):
        return iter(self._pairs)

    def add_pair(self, pair: SensorBeaconPair):
        self._pairs.append(pair)

    def impossible_positions_in_line(self, y: int) -> Set[Tuple[int, int]]:
        impossible_positions = []
        for pair in tqdm(self):
            impossible_positions.extend(pair.impossible_positions_in_line(y=y))
        return set(impossible_positions) - self.beacons()

    def beacons(self) -> Set[Tuple[int, int]]:
        return {p.beacon_position for p in self}

    def sensors(self) -> Set[Tuple[int, int]]:
        return {p.sensor_position for p in self}
