from stepFunctionBuilder import StepFunctionBuilder

def converter(xmlData):
    sf = StepFunctionBuilder('hello65', 'test defination builder')
    sf.addTask('hello', 'resource:arn', 'checkValidity')
    sf.addChoice('checkValidity', 'isValid', 'waitFor5min', 'hello1')
    sf.addWait('waitFor5min',5*60,'hello1')
    sf.addTask('hello1', 'resource:arn')
    sf.buildStepFunctionDefinition()