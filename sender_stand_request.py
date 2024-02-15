import configuration
import requests


# Функция создания заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                        json=body)


# Функция получения трека заказа
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER,
                        params={'t': track})
