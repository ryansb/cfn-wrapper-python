# MIT Licensed, Copyright (c) 2015 Ryan Scott Brown <sb@ryansb.com>

from cfn_wrapper import cfn_resource

@cfn_resource
def lambda_handler(event, context):
    # deal with your external service here
    return {
        "Status": "SUCCESS",
        "Reason": "Life is good, man",
        "PhysicalResourceId": "some:fake:id",
        "Data": {},
    }
