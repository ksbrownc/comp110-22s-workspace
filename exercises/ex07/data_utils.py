"""Dictionary related utility functions."""

__author__ = "730327035"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
   
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader: 
        result.append(row)

    # Close the file wen we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a lsit[[str] of all values in a single column."""
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


def head(table_columns: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Column based table with only the first few rows of data to easily display data."""
    result: dict[str, list[str]] = {}

    for key in table_columns:
        if n >= len(table_columns[key]):
            return table_columns
        elements: list[str] = []
        i: int = 0
        while i < n: 
            elements.append(table_columns[key][i])
            i += 1
        result[key] = elements

    return result


def select(columnbased: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """This function views the first few rows of the column and organizes to what is important."""
    results: dict[str, list[str]] = {}
    for column in names:
        results[column] = columnbased[column] 
    return results
    

def concat(columned: dict[str, list[str]], acolumn: dict[str, list[str]]) -> dict[str, list[str]]:
    """A new column based table that would combine two columns with different sources."""
    result: dict[str, list[str]] = {}
    for key in columned:
        result[key] = columned[key]
    for key in acolumn:
        if key in result:
            result[key] += acolumn[key]
        else:
            result[key] = acolumn[key]
    
    return result


def count(alist: list[str]) -> dict[str, int]:
    """Simple Anlaysis that counts frequency of values that appears on the table."""
    result: dict[str, int] = {}
    for value in alist:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result