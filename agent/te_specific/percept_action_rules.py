two_tile = [
    {
        'condition': (lambda percepts: percepts[0]),
        'action': 'SUCK'
    },
    {
        'condition': (lambda percepts: percepts[1] == (0,0)),
        'action': 'RIGHT'
    },
    {
        'condition': (lambda percepts: percepts[1] == (1,0)),
        'action': 'LEFT'
    }
]

stochastic_2d = [
    {
        'condition': (lambda percepts: percepts[0]),
        'actions': [
            (1.0, 'SUCK')
        ]
    },
    {
        'condition': (lambda percepts: not percepts[0]),
        'actions': [
            (0.25, 'UP'),
            (0.25, 'DOWN'),
            (0.25, 'LEFT'),
            (0.25, 'RIGHT')
        ]
    }
]