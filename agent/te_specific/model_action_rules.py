two_tile = [
    {
        'condition': (lambda model: model.vacuum_location not in model.cleaned_tiles),
        'action': 'SUCK'
    },
    {
        'condition': (lambda model: model.vacuum_location == (0,0) and (1,0) not in model.cleaned_tiles),
        'action': 'RIGHT'
    },
    {
        'condition': (lambda model: model.vacuum_location == (1,0) and (0,0) not in model.cleaned_tiles),
        'action': 'LEFT'
    }
]