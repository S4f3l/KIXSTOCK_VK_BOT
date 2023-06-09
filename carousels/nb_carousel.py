import json
from vktools import Carousel

nb_sn_carousel = {
    "type": "carousel",
    "elements": [

        {
            "photo_id": "-221044024_457239024",
            "action": {
                "type": "open_photo"
            },
            "buttons": [
                {
                    "action": {
                        "type": "open_link",
                        "link": "https://vk.com/market-220253762?screen=group&w=product-220253762_8012097%2Fquery",
                        "label": "New Balance NB 2002R",
                        "payload": "{}"
                }
            }]
        }
    ]
}
nb_sn_carousel = json.dumps(nb_sn_carousel, ensure_ascii=False).encode('utf-8')
nb_sn_carousel = str(nb_sn_carousel.decode('utf-8'))

nb_out_carousel = {
    "type": "carousel",
    "elements": [

        {
            "photo_id": "-221044024_457239031",
            "action": {
                "type": "open_photo"
            },
            "buttons": [
                {
                    "action": {
                        "type": "open_link",
                        "link": "-221044024_457239031",
                        "label": "New Balance Logo",
                        "payload": "{}"
                }
            }]
        }
    ]
}
nb_sn_carousel = json.dumps(nb_sn_carousel, ensure_ascii=False).encode('utf-8')
nb_sn_carousel = str(nb_sn_carousel.decode('utf-8'))