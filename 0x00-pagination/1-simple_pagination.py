#!/usr/bin/env python3
"""
This module implement a simple pagination for a CSV file.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple containing a start index and an end index corresponding to
    the range of indexes to return in a list for those particular pagination
    parameters.
    """
    if page and page_size:  # if page and page_size are not None
        start = (page - 1) * page_size  # calculate start index for the range
        end = page * page_size  # calculate end index of range
        return (start, end)
    else:  # if page or page_size is None
        return (0, 0)  # return a tuple with start and end index of range as 0


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"  # the name of the data file

    def __init__(self):  # constructor
        self.__dataset = None

    def dataset(self) -> List[List]:  # getter for dataset
        """Cached dataset
        """
        if self.__dataset is None:  # if dataset is not cached
            with open(self.DATA_FILE) as f:  # open the data file and read it
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # cache the dataset

        return self.__dataset  # return the dataset object from the cache

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)  # get start and end index
        pages = []  # initialize an empty list to store the pages
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()  # initialize the pages list with the dataset
        return pages[start:end]  # return the page of the dataset
