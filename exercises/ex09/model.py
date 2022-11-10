"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730577405"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> int:
        """Distance between two points."""
        length: float = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return length


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Immunity following recovery."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
    
    def contract_disease(self) -> None:
        """Causes cell to be infected."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Determines if the cell is infected."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
        
    def is_infected(self) -> bool:
        """Determines infected cell."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def is_immune(self) -> bool:
        """Gives immunity to cell."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
    
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "red"
        if self.is_immune():
            return "green"

    def contact_with(self, another: Cell) -> None:
        """Makes cells infected with interactions."""
        if self.is_infected() is True and another.is_vulnerable() is True:
            another.contract_disease()
        if another.is_infected() is True and self.is_vulnerable() is True:
            self.contract_disease()
    
    def immunize(self) -> None:
        """Gives immunization to some cells."""
        self.sickness = constants.IMMUNE


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, number: int, immunized: int = 0):
        """Initialize the cells with random locations and directions."""
        if number <= 0 or number >= cells:
            raise ValueError("Some number of cells must begin as infected.")
        if immunized + number >= cells:
            raise ValueError()
        if immunized < 0 or immunized >= cells:
            raise ValueError()
        self.population = []
        for _ in range(cells - number - immunized):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(number):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            infected: Cell = Cell(start_location, start_direction)
            infected.contract_disease()
            self.population.append(infected)
        for _ in range(immunized):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            immune: Cell = Cell(start_location, start_direction)
            immune.immunize()
            self.population.append(immune)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
    
    def check_contacts(self) -> None:
        """Checks the collision of points."""
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1
                
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        while i < len(self.population):
            if self.population[i].is_infected():
                return False
            i += 1
        return True