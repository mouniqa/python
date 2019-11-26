def ll(module):
    '''Returns the attributes of given module excluding dunder functions.'''
    attributes = [item for item in dir(module) if '__' not in item]
    no_of_dunder_funcs = len([item for item in dir(module) if '__' in item])
    print('.........')
    print('Size: ',len(attributes))
    print('(Excluded',no_of_dunder_funcs,'dunder functions.)')
    print('.........')
    for i in attributes:
        print(i)
    print('.........')
