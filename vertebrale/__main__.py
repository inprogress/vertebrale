#!usr/bin/env python

from flask import Flask

from vertebrale.database import db_session, init_db
from flask_graphql import GraphQLView
from vertebrale.schema import schema
from vertebrale.importer import startImport

app = Flask(__name__)
#app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
    schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exeption=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    startImport()
    app.run()
