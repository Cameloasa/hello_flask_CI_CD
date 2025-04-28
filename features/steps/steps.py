from behave import given, then, when
from app.main import app

@given(u'the Flask app is running')
def step_impl_given(context):
    context.client = app.test_client()

@when(u'I visit the home page')
def step_impl_when(context):
    context.response = context.client.get('/')

@then(u'I should see "Hello, Flask!"')
def step_impl_then(context):
    assert b"Hello, Flask!" in context.response.data
