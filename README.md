
# Mensajes ROS
Este repositorio define los mensajes utilizados por el protocolo ROS, en formato protobuf. Este protocolo busca transmitir requests _http_ usando redes celular, de la manera mas eficiente posible.

El cliente codifica y comprime los mensajes, para luego enviarlos a un backend propio que se encarga de realizar el request correspondiente en internet.
Ver un ejemplo de implementación de SDK para Flutter en [ros-flutter](https://github.com/RequestOverSMS/ros-flutter)
## Request

```protobuf
message ROSRequest {

  optional Type    type    = 1 [default = REQUEST];
  optional Method  method  = 2;
  // 3 reserved for ROSResponse
  optional string  uri     = 4;
  optional bytes   headers = 5;
  optional bytes   body    = 6;
}
```

## Response
```protobuf
message ROSResponse {

  optional Type    type    = 1 [default = RESPONSE];
  optional Method  method  = 2;
  optional uint32  code    = 3;
  // 4 reserved in ROSRequest
  optional bytes   headers = 5;
  optional bytes   body    = 6;
}
```

