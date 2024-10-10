
def prefix_decorator(prefix):
    def decorator_function(original_func):
        def wrapper_function(*args, **kwargs):
            print(prefix,'Executed Before', original_func.__name__)
            result = original_func(*args, **kwargs)
            print(prefix,'Executed After', original_func.__name__,'\n')
            return result
        
        return wrapper_function
    return decorator_function


@prefix_decorator('Testing:')
def display_info(name, age):
    print(f'Display_info ran with arguments ({name}, {age})')
    

display_info('Naga Mahesh Gatta', 25)
display_info('Travis', 30)