import jwt

encoded = jwt.encode({'username':'scared','admin':'true'},'secret',algorithm='HS256')

print(encoded)