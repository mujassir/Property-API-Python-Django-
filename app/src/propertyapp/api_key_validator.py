
from propertyapp.constants import Constants

# Validates API Key
class APIKeyValidator:
    def Validate(apiKey):
        keys = Constants.APIKEYS
        if(keys.__contains__(apiKey)):
            return True
        return False
