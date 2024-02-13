from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    '''
    Custom Pagination class can be modified based on the data load
    '''
    default_limit = 25
    limit_query_param = 10
    offset_query_param = 25