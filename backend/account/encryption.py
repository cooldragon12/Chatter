from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization




class Encryption:
    
    def __init__(self, privateKey:rsa.RSAPrivateKey = None): # type: ignore
        if privateKey :
            self.privateKey = privateKey
            self.publicKey = self.privateKey.public_key()
        else:
            self.privateKey = self.createPrivateKeyRSA()
            self.publicKey = self.privateKey.public_key()
    
    def serializePrivateKey(self):
        return self.privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    def serializePublicKey(self):
        return self.publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    def loadSerializedPrivateKey(self, serializedPrivateKey:bytes):
        """Load private key from serialized private key"""
        return serialization.load_pem_private_key(
            serializedPrivateKey,
            password=None,
        )
    def loadSerializedPublicKey(self, serializedPublicKey:bytes):
        """Load public key from serialized public key"""
        return serialization.load_pem_public_key(
            serializedPublicKey,
        )
    def encrypt(self, message:str):
        messages = message.encode('utf-8')
        encryptedMessage = self.publicKey.encrypt(
            messages,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            )
        )
        return encryptedMessage

    def decrypt(self, encryptedMessage:bytes):
        decryptedMessage = self.privateKey.decrypt(
            encryptedMessage,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            )
        )
        decryptedMessage = decryptedMessage.decode('utf-8')
        return decryptedMessage
    
    @staticmethod
    def createPrivateKeyRSA(keysize:int=2048):
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=keysize,
        )
        return key