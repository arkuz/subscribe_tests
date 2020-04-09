import requests as req


class API(object):
    """ Класс описывает endpoints API """

    def __init__(self, url):
        self.url = url


    def call_post_api(self, url, data={}, params={}):
        """ Обертка над requests.post """
        resp = req.post(
            url,
            data=data,
            params=params,
        )
        return resp


    def call_get_api(self, url, params={}):
        """ Обертка над requests.get """
        resp = req.get(
            url,
            params=params,
        )
        return resp


    def call_delete_api(self, url, params={}, data={}):
        """ Обертка над requests.delete """
        resp = req.delete(
            url,
            data=data,
            params=params,
        )
        return resp


    def add_subscriber(self, data={}):
        endpoint = '/subscriptions'
        url = self.url + endpoint
        return self.call_post_api(url, data=data)


    def get_subscribers(self):
        endpoint = '/subscriptions'
        url = self.url + endpoint
        return self.call_get_api(url)


    def delete_subscribers(self):
        endpoint = '/subscriptions'
        url = self.url + endpoint
        return self.call_delete_api(url)

