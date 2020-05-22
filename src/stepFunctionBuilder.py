import json
'''
This Step function builder will help constructing AWS step fucntion definition programmatically by calling fucntion.
'''
class StepFunctionBuilder:
    def __init__(self, startAt, comment):
        self.sf_definition = {
            'Comment': comment,
            'StartAt': startAt,
            'States': {}
        }
        self.buildSuccess = False
        
    # Add task in definition.
    def addTask(self, name, resource, nextTask=None):
        if nextTask is not None:
            self.sf_definition['States'].update({
                name: {
                    'Type': 'Task',
                    'Resource': resource,
                    'Next': nextTask
                }
            })
        else:
            self.sf_definition['States'].update({
                name: {
                    'Type': 'Task',
                    'Resource': resource,
                    "End": True
                }
            })
    # Add wait state in definition.
    def addWait(self, name, waitTime, nextTask):
        self.sf_definition['States'].update({
            name: {
                'Type': 'Wait',
                "Seconds": waitTime,
                'Next': nextTask
            }
        })

    # Add choice state in definition.
    def addChoice(self, name, checkVariableName, nextForTrue, nextForFalse):
        self.sf_definition['States'].update({
            name: {
                'Type': 'Choice',
                "Choices": [
                    {
                        "Variable": "$."+checkVariableName,
                        "BooleanEquals": True,
                        "Next": nextForTrue
                    },
                    {
                        "Variable": "$."+checkVariableName,
                        "BooleanEquals": False,
                        "Next": nextForFalse
                    }
                ]
            }
        })

    # Build step function definition.
    def buildStepFunctionDefinition(self):
        states = self.sf_definition['States']
        if self.validateStates():
            self.buildSuccess = True

    # Validate step function definition if all state has valid next state.
    def validateStates(self):
        states = self.sf_definition['States']
        if self.sf_definition['StartAt'] not in states:
            return False

        for key, value in states.items():
            if value['Type'] == 'Task' or value['Type'] == 'Wait':
                if 'End' in value:
                    pass
                elif value['Next'] not in states:
                    return False
            elif value['Type'] == 'Choice':
                for choice in value['Choices']:
                    if choice['Next'] not in states:
                        return False
        return True

    # Returns definition after building the step function.
    def getStepFunctionDefinition(self):
        if self.buildSuccess:
            return json.dumps(self.sf_definition)
        
        return "Not build"

# Driving main function for this script.
if __name__ == "__main__":
    # Creating new object
    sf = StepFunctionBuilder(startAt='hello65', comment='test defination builder')
    # Added new task state
    sf.addTask(name='hello', resource='resource:arn', nextTask='checkValidity')
    #Added new choice state 
    sf.addChoice(name='checkValidity', checkVariableName='isValid', nextForTrue='waitFor5min', nextForFalse='hello1')
    #Added new wait state
    sf.addWait(name='waitFor5min', waitTime=5 * 60, nextTask='hello1')
    
    # Default next will be End if next task is not provided.
    sf.addTask(name='hello1', resource='resource:arn')

    # First need to buil the step fucntion which will first validate the step function definition then mark build flag as true to fetch definition.
    sf.buildStepFunctionDefinition()

    # Fetiching step function definition.
    print(sf.getStepFunctionDefinition())
    

