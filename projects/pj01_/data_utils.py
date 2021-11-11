"""Utility functions."""

__author__ = "123456789"

from csv import DictReader


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Reads and Adds rows from a csv."""
    table: list[dict[str, str]] = []

    # Opens the file
    file_handle = open(path, "r", encoding="utf8")

    # Read CSV File
    csv_reader = DictReader(file_handle)

    # Reads Each Row, line by line
    for row in csv_reader:
        table.append(row)

    # Close File
    file_handle.close()

    return table


def column_values(list_rows: list[dict[str, str]], col_name: str) -> list[str]:
    """Produces a list of all values in a specified column."""
    col_list: list[str] = []

    for row in list_rows:
        col_list.append(row[col_name])

    return col_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented to colunm-oriented."""
    return_table: dict[str, list[str]] = {}

    first_row: dict[str, str] = table[0]

    for column in first_row:
        return_table[column] = column_values(table, column)

    return return_table


def head(table: dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
    """Returns the number of rows specified."""
    head_table: dict[str, list[str]] = {}

    if row_num > len(table):
        row_num = len(table)

    for column in table:
        # Empty list of strings
        column_values: list[str] = []

        # This will help us count times through the loop
        i: int = 0

        # column is a list[str], so we are going through each value in list
        for i in range(row_num):
            # checks if have gone the number of times desired
            if (i < row_num):
                column_values.append(table[column][i])

        # Now add to the new table
        head_table[column] = column_values

    return head_table


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Returns a Table of only specified columns."""
    selected_table: dict[str, list[str]] = {}

    # Loop through each selected column name
    for name in col_names:
        # Add name and access values from the original table
        selected_table[name] = table[name]
    return selected_table


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table that combines two tables."""
    concat_table: dict[str, list[str]] = {}

    # Loop through each column in table_1 and add contents to concat_table
    for column in table_1:
        concat_table[column] = table_1[column]

    # Loop through each column in table_2
    for column in table_2:
        # If already in table, add on to it
        if column in concat_table:
            concat_list: list[str] = concat_table[column] + table_2[column]
            concat_table[column] = concat_list
        else:
            concat_table[column] = table_2[column]

    return concat_table


def count(values: list[str]) -> dict[str, int]:
    """Returns a dictionary that counts unique values."""
    dictionary: dict[str, int] = {}
    for item in values:
        if item in dictionary:
            dictionary[item] = dictionary[item] + 1
        else:
            dictionary[item] = 1
    return dictionary
