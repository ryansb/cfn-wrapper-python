import cfn_resource


class FakeLambdaContext(object):
    def __init__(self, name='Fake', version='LATEST'):
        self.name = name
        self.version = version

    @property
    def get_remaining_time_in_millis(self):
        return 10000

    @property
    def function_name(self):
        return self.name

    @property
    def function_version(self):
        return self.version

    @property
    def invoked_function_arn(self):
        return 'arn:aws:lambda:123456789012:' + self.name

    @property
    def memory_limit_in_mb(self):
        return 1024

    @property
    def aws_request_id(self):
        return '1234567890'


def wrap_with_mock(func, base_response=None):
    def wrapper(*args):
        return func(*args)
    return wrapper


base_event = {
    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/SomeStackHere3/d50d1280-a454-11e5-bd51-50e2416294a8",
    "ResponseURL": "https://cloudformation-custom-resource-response-useast1.s3.amazonaws.com/arn%3Aaws%3Acloudformation%3Aus-east-1%3A368950843917%3Astack/SomeStackHere3/d50d1280-a454-11e5-bd51-50e2416294a8%7CFakeThing%7C79abbda7-092e-4534-9602-3ab4cc377807?AWSAccessKeyId=AKIAJNXHFR7P7YGKLDPQ&Expires=1450321030&Signature=HOCkeEsxMHHQMgnj3kx5gqLyfTU%3D",
    "ResourceProperties": {
        "OtherThing": "foobar",
        "ServiceToken": "arn:aws:lambda:us-east-1:123456789012:function:PyRsrc",
        "AnotherThing": "2"
    },
    "RequestType": "Delete",
    "ServiceToken": "arn:aws:lambda:us-east-1:123456789012:function:PyRsrc",
    "ResourceType": "Custom::MyResource",
    "PhysicalResourceId": "SomeStackHere3-FakeThing-893YUKO12RFM",
    "RequestId": "79abbda7-092e-4534-9602-3ab4cc377807",
    "LogicalResourceId": "FakeThing"
}


cfn_resource.wrap_user_handler = wrap_with_mock


def test_wraps_func():
    rsrc = cfn_resource.Resource()
    @rsrc.delete
    def delete(event, context):
        return {"status": cfn_resource.FAILED}
    resp = rsrc(base_event.copy(), FakeLambdaContext())
    assert(resp['status'] == 'FAILED')
