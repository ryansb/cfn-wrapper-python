# MIT Licensed, Copyright (c) 2015 Ryan Scott Brown <sb@ryansb.com>

import cfn_resource

# set `handler` as the entry point for Lambda
handler = cfn_resource.Resource()

@handler.create
def create_thing(event, context):
    # do some stuff
    return {"PhysicalResourceId": "arn:aws:fake:myID"}

@handler.update
def update_thing(event, context):
    # do some stuff
    return {"PhysicalResourceId": "arn:aws:fake:myID"}
