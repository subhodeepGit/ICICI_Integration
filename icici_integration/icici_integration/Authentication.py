
# import org.apache.commons.codec.binary.Base64;
# import org.apache.commons.codec.binary.Hex;
# import org.apache.commons.codec.digest.HmacAlgorithms;
# import org.apache.commons.codec.digest.HmacUtils;

# public class Example {
# public static void main(String[] args) {
# final HmacUtils hmacHelper = new HmacUtils(HmacAlgorithms.HMAC_SHA_256, API_SECRET);
# final Hex hexHelper = new Hex();

# final String msg = API_KEY + CLIENT_REQUEST_ID + TIMESTAMP + JSON_SERIALIZED_PAYLOAD;
# final byte[] raw = hmacHelper.hmac(msg);
# final byte[] hex = hexHelper.encode(raw);
# final String messageSignature = Base64.encodeBase64String(hex);
# }
# }
from __future__ import print_function
import openapi_client
import simple
from simple import MerchantCredentials
from simple import Gateway
from openapi_client.rest import ApiException
from pprint import pprint
import json

api_key = "6SYuaKoauAVjSsbQTfcMMlrqZG4y8yDs"
api_secret = "6wVmRYzk5XoZvQKkQOHPteL8Uy4N9e5PI6jRqbqNoGh"

credentials = MerchantCredentials(api_key, api_secret)

gateway = Gateway.create(credentials)
api_client = openapi_client.ApiClient()

json_payload = 	"""{
					\"requestType\": \"PaymentCardSaleTransaction\",
					\"transactionAmount\": {
						\"total\": \"25.01\",
						"currency": "USD"
					},
					\"paymentMethod\": {
						\"paymentCard\": {
							\"number\": \"4012000033330026\",
							\"expiryDate\": {
								\"month\": \"12\",
								\"year\": \"25\"
							},
							\"securityCode\": \"977\"
						}
					}
				}"""

obj_name = "PaymentCardSaleTransaction"
obj_model = getattr(openapi_client, obj_name)
payload = api_client.build_object(json.loads(json_payload), obj_model)

result = gateway.primary_payment_transaction(payload)
pprint(result)