from rest_framework.pagination import PageNumberPagination

class PollPanination(PageNumberPagination):
    page_size = 1
    page_size_query_param = "page size"
    max_page_size = 1000