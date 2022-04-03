requestStr = """{
  "additional_info": {
    "items": [
      {
        "id": "PR0001",
        "title": "Point Mini",
        "description": "Producto Point para cobros con tarjetas mediante bluetooth",
        "picture_url": "https://http2.mlstatic.com/resources/frontend/statics/growth-sellers-landings/device-mlb-point-i_medium@2x.png",
        "category_id": "electronics",
        "quantity": 1,
        "unit_price": 58.8
      }
    ],
    "payer": {
      "first_name": "Test",
      "last_name": "Test",
      "phone": {
        "area_code": 11,
        "number": "987654321"
      },
      "address": {}
    },
    "shipments": {
      "receiver_address": {
        "zip_code": "12312-123",
        "state_name": "Rio de Janeiro",
        "city_name": "Buzios",
        "street_name": "Av das Nacoes Unidas",
        "street_number": 3003
      }
    },
    "barcode": {}
  },
  "description": "Payment for product",
  "external_reference": "MP0001",
  "installments": 1,
  "metadata": {},
  "order": {
    "type": "mercadolibre"
  },
  "payer": {
    "entity_type": "individual",
    "type": "customer",
    "identification": {}
  },
  "payment_method_id": "visa",
  "transaction_amount": 58.8
}"""

responseStr = """{
  "id": 20359978,
  "date_created": "2019-07-10T14:47:58.000Z",
  "date_approved": "2019-07-10T14:47:58.000Z",
  "date_last_updated": "2019-07-10T14:47:58.000Z",
  "money_release_date": "2019-07-24T14:47:58.000Z",
  "issuer_id": 25,
  "payment_method_id": "visa",
  "payment_type_id": "credit_card",
  "status": "approved",
  "status_detail": "accredited",
  "currency_id": "BRL",
  "description": "Point Mini a maquininha que dá o dinheiro de suas vendas na hora",
  "taxes_amount": 0,
  "shipping_amount": 0,
  "collector_id": 448876418,
  "payer": {
    "id": 123,
    "email": "test_user_80507629@testuser.com",
    "identification": {
      "number": 19119119100,
      "type": "CPF"
    },
    "type": "customer"
  },
  "metadata": {},
  "additional_info": {
    "items": [
      {
        "id": "PR0001",
        "title": "Point Mini",
        "description": "Producto Point para cobros con tarjetas mediante bluetooth",
        "picture_url": "https://http2.mlstatic.com/resources/frontend/statics/growth-sellers-landings/device-mlb-point-i_medium@2x.png",
        "category_id": "electronics",
        "quantity": 1,
        "unit_price": 58.8
      }
    ],
    "payer": {
      "registration_date": "2019-01-01T15:01:01.000Z"
    },
    "shipments": {
      "receiver_address": {
        "street_name": "Av das Nacoes Unidas",
        "street_number": 3003,
        "zip_code": 6233200,
        "city_name": "Buzios",
        "state_name": "Rio de Janeiro"
      }
    }
  },
  "order": {},
  "external_reference": "MP0001",
  "transaction_amount": 58.8,
  "transaction_amount_refunded": 0,
  "coupon_amount": 0,
  "transaction_details": {
    "net_received_amount": 56.16,
    "total_paid_amount": 58.8,
    "overpaid_amount": 0,
    "installment_amount": 58.8
  },
  "fee_details": [
    {
      "type": "coupon_fee",
      "amount": 2.64,
      "fee_payer": "payer"
    }
  ],
  "statement_descriptor": "MercadoPago",
  "installments": 1,
  "card": {
    "first_six_digits": 423564,
    "last_four_digits": 5682,
    "expiration_month": 6,
    "expiration_year": 2023,
    "date_created": "2019-07-10T14:47:58.000Z",
    "date_last_updated": "2019-07-10T14:47:58.000Z",
    "cardholder": {
      "name": "APRO",
      "identification": {
        "number": 19119119100,
        "type": "CPF"
      }
    }
  },
  "notification_url": "https://www.suaurl.com/notificacoes/",
  "processing_mode": "aggregator",
  "point_of_interaction": {
    "type": "PIX",
    "application_data": {
      "name": "NAME_SDK",
      "version": "VERSION_NUMBER"
    },
    "transaction_data": {
      "qr_code_base64": "iVBORw0KGgoAAAANSUhEUgAABRQAAAUUCAYAAACu5p7oAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAIABJREFUeJzs2luO3LiWQNFmI+Y/Zd6vRt36KGNXi7ZOBtcagHD4kNLeiLX33v8DAAAAABD879sDAAAAAAA/h6AIAAAAAGSCIgAAAACQCYoAAAAAQCYoAgAAAACZoAgAAAAAZIIiAAAAAJAJigAAAABAJigCAAAAAJmgCAAAAABkgiIAAAAAkAmKAAAAAEAmKAIAAAAAmaAIAAAAAGSCIgAAAACQCYoAAAAAQCYoAgAAAACZoAgAAAAAZIIiAAAAAJAJigAAAABAJigCA...",
      "qr_code": "00020126600014br.gov.bcb.pix0117test@testuser.com0217dados adicionais520400005303986540510.005802BR5913Maria Silva6008Brasilia62070503***6304E2CA"
    }
  }
}"""

from google.protobuf.json_format import Parse, ParseDict
from google.protobuf.json_format import MessageToJson


import json
import base64
import zlib
import rsa

from v1_payments_request_pb2 import v1_payments_request
from ROSRequest_pb2 import ROSRequest
from ROSEnums_pb2 import Method
from HTTPHeaders_pb2 import Headers

#publicKey, privateKey = rsa.newkeys(512)
message = requestStr
headers = """{
                  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
                  "Content_Type": "application/json"
                  }"""

plain = json.dumps(json.loads(message))

body = ParseDict(json.loads(message), v1_payments_request()).SerializeToString()
headers = ParseDict(json.loads(headers), Headers()).SerializeToString()


ros = ROSRequest()
ros.method = Method.GET
ros.uri = "https://api.mercadopago.com/v1/payments"
ros.headers = headers
ros.body = body

ros_plain = f"{ros}"
ros_str = ros.SerializeToString()

print()
print(f"Protobuf: {len(ros_str)}")
print(ros)

body_compressed = zlib.compress(ros_str, level=9)
plain_compressed = zlib.compress(str.encode(ros_plain), level=9) 
print()
print(f"Compressed: {len(body_compressed)} vs {len(plain_compressed)} ({(1-len(body_compressed)/len(plain_compressed))*100})")
print(body_compressed)

body_encoded = base64.b64encode(body_compressed)
plain_encoded = base64.b64encode(plain_compressed)
print()
print(f"Encoded: {len(body_encoded)} vs {len(plain_encoded)} ({(1-len(body_encoded)/len(plain_encoded))*100})")
print(body_encoded)


#body_encripted = rsa.encrypt(body_encoded,publicKey)
#plain_encripted = rsa.encrypt(plain_encoded,publicKey)

#print()
#print(f"Encoded: {len(body_encripted)} vs {len(plain_encripted)} ({(1-len(body_encripted)/len(plain_encripted))*100})")
#print(body_encripted)

################################## SEND SMS

# Decrypt
#body_encoded = rsa.decrypt(body_encripted, privateKey).decode()

# Decode
body_compressed = base64.b64decode(body_encoded)

# Decompress
body = zlib.decompress(body_compressed)

# Parse protobuf
ros_received = ROSRequest()
ros_received.ParseFromString(body)
ros_message_received = MessageToJson(ros_received)

print()
print(f"Protobuf: {len(ros_message_received)} vs {len(ros_plain)} ({(1-len(ros_message_received)/len(ros_plain))*100})")

if ros_received.uri == "https://api.mercadopago.com/v1/payments" and ros_received.method == Method.GET:
  headers = Headers()
  headers.ParseFromString(ros_received.headers)
  headers_received = MessageToJson(headers)

  body = v1_payments_request()
  body.ParseFromString(ros_received.body)
  body_received = MessageToJson(body)

  print("HEADERS:")
  print(headers_received)
  print()
  print("BODY:")
  print(body_received)





