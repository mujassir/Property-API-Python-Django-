
from propertyapp.config.configuration import Configuration

# Validates API Key
class APIKeyValidator:
    def Validate(apiKey):
        keys = Configuration.APIKEYS
        if(keys.__contains__(apiKey)):
            return True
        return False
