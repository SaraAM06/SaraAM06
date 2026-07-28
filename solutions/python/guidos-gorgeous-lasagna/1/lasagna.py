#Task 1

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 #Task 3

#Task 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining
    
    Parameters:
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.

    Returns:
        int: The bake time remaining (in minutes).

    This function takes one integer representing the elapsed cooking time and calculates the bake
    time remaining (EXPECTED_BAKE_TIME - elapsed_bake_time).
    
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

#Task 3
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time

    Parameters:
        number_of_layers (int): The number of layers in the lasagna

    Returns:
        int: The preparation time in minutes

    This function takes one integer representing the number of lasagna 
    layers and calculates the preparation time in minutes (number_of_layers * PREPARATION_TIME).
    """
    return number_of_layers * PREPARATION_TIME


#Task 4
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    time_layering = preparation_time_in_minutes(number_of_layers)
    return time_layering + elapsed_bake_time
