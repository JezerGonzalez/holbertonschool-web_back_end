#!/usr/bin/env python3
"""Simple pagination"""
from typing import Tuple, List, Dict
import csv


def index_range(page: int, page_size: int) -> Tuple:
    """Simple helper function"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get my data"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = Server.dataset(self)
        pages = index_range(page, page_size)
        return data[pages[0]:pages[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Your mom"""
        data = Server.dataset(self)
        totalPages = (len(data) + page_size - 1) // page_size
        nextPage = page + 1 if page < totalPages else None
        prevPage = page - 1 if page > 1 else None
        currentPage = Server.get_page(self, page, page_size)
        return {
            'page_size': page_size,
            'page': page,
            'data': currentPage,
            'next_page': nextPage,
            'prev_page': prevPage,
            'total_pages': totalPages
        }
