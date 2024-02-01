#!/usr/bin/env python3
"""
This is a simple helper function that takes two integers arguments and returns
a tuple containing a start index and an end index corresponding to the range
of indexes to return in a list for those particular pagination parameters.
"""


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
