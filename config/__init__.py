"""
Configuration package
"""

def configure(app):
    """
    Configure the given app

    WARN: Make sure DEBUG is set to False in production. Leaving it on will allow users to run
    arbitrary Python code on your server.
    """
    app.config.from_object('config.default')

    # HACKED. Environment
    # app.config.from_envvar('APP_CONFIG_FILE')
    is_development = True
    config_file = 'config.development' if is_development else 'config.production'
    app.config.from_object(config_file)

    # Add instance specific config
    # Instance specific config contain sensitive information, such as secret key, API tokens,
    # or database URIs
    app.config.from_pyfile('config.py')
