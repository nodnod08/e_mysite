from django.core.paginator import Paginator

class MyPaginator:

    def __init__(self, query_set = None, limit = 10):
        self.query_set = query_set
        self.limit = limit
        self.paginated = Paginator(self.query_set, self.limit)

    def do_paginate(self, page):
        action = self.paginated.page(page)
        result = action.object_list
        total = self.paginated.count
        has_prev = action.has_previous()
        has_next = action.has_next()
        num_pages = self.paginated.num_pages

        data_from = (((int(page) - 1) * int(self.limit)) + 1) if len(result) else 0
        data_to = (((int(page) - 1) * int(self.limit)) + int(self.limit)) if int(page) < int(num_pages) else (((int(page) - 1) * int(self.limit)) + len(result))

        data = {
            "current": int(page),
            "prev_page": int(page) - 1 if int(page) != int(num_pages) and int(page) > 1 else None,
            "next_page": int(page) + 1 if int(page) != int(num_pages) and int(page) < int(num_pages) else None,
            "data": result,
            "total": total,
            "has_prev": has_prev,
            "has_next": has_next,
            "pages": num_pages,
            "per_page": self.limit,
            "from": data_from,
            "to": data_to,
        }

        return data