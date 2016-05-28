"""
Identity Utilities
XXX: Most of the following have not been implemented.
     They're defined as placeholder utility functions for the purpose
     of satisfying DB requirements in blogger.models
"""
def get_user():
    """
    Returns the current user accessing the app.
    XXX: For now, hardcode to always use me as the user.
    """
    return 'abekim'

def encrypt(text=''):
    if not text or type(text) is not str:
        # Log to the app or do something
        return ''

    return 'user0abekim'

def generate_temp_password():
    """
    Generates a temporary password to be 
    XXX: For now, return my string
    """
    return 'user0abekim'

# Implement a validate function on the client side. Test for password rules client side!
