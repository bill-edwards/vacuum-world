standard = [
    {
        'action': 'SUCK',
        'state_transform': (lambda state: state.clean_tile(state.vacuum_location))
    },
    {
        'action': 'RIGHT',
        'state_transform': (lambda state: state.move_vacuum('RIGHT'))
    },
    {
        'action': 'LEFT',
        'state_transform': (lambda state: state.move_vacuum('LEFT'))
    },
    {
        'action': 'UP',
        'state_transform': (lambda state: state.move_vacuum('UP'))
    },
    {
        'action': 'DOWN',
        'state_transform': (lambda state: state.move_vacuum('DOWN'))
    },
    {
        'action': 'NONE',
        'state_transform': (lambda state: state)
    }
]

slippery = [
    {
        'action': 'SUCK',
        'state_transform': (lambda state: state.clean_tile(state.vacuum_location))
    },
    {
        'action': 'RIGHT',
        'state_transforms': [
            (0.75, (lambda state: state.move_vacuum('RIGHT'))),
            (0.25, (lambda state: state))
        ]
    },
    {
        'action': 'LEFT',
        'state_transforms': [
            (0.75, (lambda state: state.move_vacuum('LEFT'))),
            (0.25, (lambda state: state))
        ]
    },
    {
        'action': 'UP',
        'state_transforms': [
            (0.75, (lambda state: state.move_vacuum('UP'))),
            (0.25, (lambda state: state))
        ]
    },
    {
        'action': 'DOWN',
        'state_transforms': [
            (0.75, (lambda state: state.move_vacuum('DOWN'))),
            (0.25, (lambda state: state))
        ]
    },
    {
        'action': 'NONE',
        'state_transform': (lambda state: state)
    }
]
