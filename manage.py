from flask_script import Manager , Server

from app import create_app
app=create_app()

manager =  Manager(app)
manager.add_command('runserver',Server(use_debugger=True))

if __name__=="__main__":
    manager.run()