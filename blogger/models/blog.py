"""
### NOTE
- save class method for db.Document is equivalent to operation merge
- We can append a '-' or a '+' to any column name in the meta data to indicate descending vs ascending order
"""

from blogger import db, utils
import datetime

class Post(db.Document):
    """
    Post model
    """
    # Schema
    author = db.StringField(required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))  # List of references
    created = db.DateTimeField(default=datetime.datetime.now, required=True)
    slug = db.StringField(max_length=200, required=True)  # Is this going to be a problem if I define the default value in the save method?
    subject = db.StringField(max_length=200, required=True)
    # Meta data / indexes
    meta = {
        'allow-inheritance': True,
        'indexes': ['-created', 'slug'],
        'ordering': ['-created'],
    }

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # Implement default values that depend on other fields
        if not self.slug:
            self.slug = utils.slugify(self.subject)

        return super(Post, self).save(*args, **kwargs)


class Comment(db.EmbeddedDocument):
    created = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.ReferenceField(User, required=True)
