"""Dictionary related utility functions."""

__author__ = "730577405"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(first: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """See the first N rows of data for each column."""
    y: dict[str, list[str]] = {}
    if N >= len(first):
        return first
    if N == 0:
        empty: list[str] = []
        for a in first:
            y[a] = empty
        return y
    for i in first:
        z: list[str] = []
        j: int = 0
        while j < N:
            z.append(first[i][j])
            j += 1
        y[i] = z
    return y


def select(one: dict[str, list[str]], two: list[str]) -> dict[str, list[str]]:
    """Select specific columns to return."""
    result: dict[str, list[str]] = {}
    for column in two:
        result[column] = one[column]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Create a column-based table from combining two column-based tables."""
    combined: dict[str, list[str]] = {}
    for column in x:
        combined[column] = x[column]
    for column in y:
        if column in combined:
            combined[column] += y[column]
        else:
            combined[column] = y[column]
    return combined


def count(idk: list[str]) -> dict[str, int]:
    """Displays number of times each string is displayed."""
    new: dict[str, int] = {}
    i: int = 0
    while i < len(idk):
        if idk[i] in new:
            new[idk[i]] += 1
        else:
            new[idk[i]] = 1
        i += 1
    return new