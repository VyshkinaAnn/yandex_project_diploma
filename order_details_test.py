# Анна Вышкина, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def test_order_details_track():
    create_order_response = sender_stand_request.post_new_order(data.order_body).json()
    get_track = sender_stand_request.get_order_track(track=(create_order_response['track']))

    assert get_track.status_code == 200
