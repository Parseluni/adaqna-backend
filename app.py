from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listPersons_resolver, getPerson_resolver
from api.mutations import create_person_resolver, update_person_resolver, delete_person_resolver
from api.queries import listQuestions_resolver, getQuestion_resolver
from api.mutations import create_question_resolver, update_question_resolver, delete_question_resolver


query = ObjectType("Query")
mutation = ObjectType("Mutation")

### PERSON QUERIES ###
query.set_field("listPersons", listPersons_resolver)
query.set_field("getPerson", getPerson_resolver)

### PERSON MUTATIONS ###
mutation.set_field("createPerson", create_person_resolver)
mutation.set_field("updatePerson", update_person_resolver)
mutation.set_field("deletePerson", delete_person_resolver)

### QUESTION QUERIES ###
query.set_field("listQuestions", listQuestions_resolver)
query.set_field("getQuestion", getQuestion_resolver)

### QUESTION MUTATIONS ###
mutation.set_field("createQuestion", create_question_resolver)
mutation.set_field("updateQuestion", update_question_resolver)
mutation.set_field("deleteQuestion", delete_question_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code



