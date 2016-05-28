from blogger import db, utils
from werkzeug.security import check_password_hash

class User(db.Document):
    """
    User model
    """
    # Schema
    username = db.StringField(required=True)
    password = db.StringField(required=True)  # Again, is the required condition going to be a problem?
    fullname = db.StringField(verbose_name="Name", max_length=200, required=True)

    def save(self, *args, **kwargs):
        # Default password if not set
        if not self.password:
            self.password = utils.identity.generate_temp_password()

        return super(User, self).save(*args, **kwargs)

    @property
    def is_authenticated(self, encrypted_passcode):
        return True if encrypted_passcode == self.password else False

    def is_active(self):
        return self.is_authenticated()

    def is_anonymous(self):
        return not self.is_authenticated()
