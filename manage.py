
from app import create_app, db
from flask_script import Manager, Server
from app.models import Pitch, User, Comment
from flask_migrate import Migrate, MigrateCommand

#create app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#run unittests
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

#create shell context
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch = Pitch, Comment = Comment )

if __name__ == '__main__':
    manager.run()