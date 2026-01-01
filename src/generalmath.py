def clamp(x, minimum, maximum):
    """forces value to be in between a minimum and a maximum value

    Args:
        x (_type_): value to augment
        minimum (_type_): minimum value
        maximum (_type_): maximum value

    Returns:
        _type_: augmented value
    """    
    return max(minimum, min(x, maximum))