import json
from vktools import Carousel

j1_low_carousel = {
    "type": "carousel",
    "elements": [

        {
            "photo_id": "-221044024_457239018",
            "action": {
                "type": "open_photo"
            },
            "buttons": [
                {
                    "action": {
                        "type": "open_link",
                        "link": "https://vk.com/market-220253762?screen=group&w=product-220253762_8012102%2Fquery",
                        "label": "Air Jordan 1 Low light smoke grey",
                        "payload": "{}"
                }
            }]
        },

        {
            "photo_id": "-221044024_457239019",
            "action": {
                "type": "open_photo"
            },
            "buttons": [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/public220253762?w=product-220253762_8013609",
                    "label": 'Union x Air Jordan 1 Low KO "Sail"',
                    "payload": "{}"
                }
            }]
        },
        {
            "photo_id": "-221044024_457239028",
            "action": {
                "type": "open_photo"
            },
            "buttons": [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/market-220253762?screen=group&w=product-220253762_8012111%2Fquery",
                    "label": 'Air Jordan 1 Low "Tokyo Vintage"',
                    "payload": "{}"
                }
            },

            ]
        }
    ]
}
j1_low_carousel = json.dumps(j1_low_carousel, ensure_ascii=False).encode('utf-8')
j1_low_carousel = str(j1_low_carousel.decode('utf-8'))

nike_und_carousel = {
    "type": "carousel",
    "elements": [
        {
            "photo_id": "-221044024_457239020",
            "action": {
                "type": "open_photo"
            },
            "buttons": [
                {
                    "action": {
                        "type": "open_link",
                        "link": "https://vk.com/market-220253762?screen=group&w=product-220253762_8012107%2Fquery",
                        "label": "Nike Dri-Fit DNA logo",
                        "payload": "{}"
                }
            }]
        },

        {
            "photo_id": "-221044024_457239023",
            "action": {
                "type": "open_photo"
            },
            "buttons": [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/market-220253762?screen=group&w=product-220253762_8012103%2Fquery",
                    "label": "Nike Swoosh French Terry Short",
                    "payload": "{}"
                }
            }]
        }
    ]
}
nike_und_carousel = json.dumps(nike_und_carousel, ensure_ascii=False).encode('utf-8')
nike_und_carousel = str(nike_und_carousel.decode('utf-8'))

nike_out_carousel = {
    "type": "carousel",
    "elements": [

        {
            "photo_id": "-221044024_457239021",
            "action": {
                "type": "open_photo"
            },
            "buttons": [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/market-220253762?screen=group&w=product-220253762_8013607%2Fquery",
                    "label": "Jordan x Union",
                    "payload": "{}"
                }
            }
            ]
        }
    ]
}
nike_out_carousel = json.dumps(nike_out_carousel, ensure_ascii=False).encode('utf-8')
nike_out_carousel = str(nike_out_carousel.decode('utf-8'))
