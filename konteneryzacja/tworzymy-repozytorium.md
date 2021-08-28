
```
#https://pypi.org/project/aws-encryption-sdk/
import aws_encryption_sdk
from aws_encryption_sdk.identifiers import CommitmentPolicy


client = aws_encryption_sdk.EncryptionSDKClient()

key_arn = "arn:aws:kms:eu-west-1:398266723651:key/9a9278ca-70ee-4c46-8c00-0b258987f923"
kms_key_provider = aws_encryption_sdk.StrictAwsKmsMasterKeyProvider(key_ids=[ key_arn ])

my_plaintext = b'This is some super secret data!  Yup, sure is!'

print();
print("Source Text:");
print(my_plaintext);

my_ciphertext, encryptor_header = client.encrypt(
    source=my_plaintext,
    key_provider=kms_key_provider
)

print();
print();
print("Encrypted Text:");
print(my_ciphertext);

decrypted_plaintext, decryptor_header = client.decrypt(
    source=my_ciphertext,
    key_provider=kms_key_provider
)

print();
print();
print("Decrypted Text:");
print(decrypted_plaintext);
```