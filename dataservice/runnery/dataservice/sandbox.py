import jwt
private_key ="""
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""

encoded = jwt.encode({"aud": "dataservice.runnery.com"}, private_key, algorithm="RS512")
print(encoded)