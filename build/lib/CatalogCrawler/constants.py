HEADERS = {
            'user-agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        }

CRAWLER_STATUS = {
    'success': 0,  # successfully get the page
    'non_200': 1,  # get request success, but get non-200 status code
    'get_error': 2  # get request fail
}

CRAWL_SUCCESS = 0
CRAWL_NON_200 = 1
CRAWL_GET_ERROR = 2