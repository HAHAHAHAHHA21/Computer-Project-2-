def mandelbrot_generator(x: complex, y: int) -> complex:
    """Generates the y'th term of the mandelbrot sequence with initial term x

    Parameters:
        x [complex]: the initial term
        y [int]: the term to generate

    Returns:
        complex: the y'th term of the mandelbrot sequence

    """

    if y == 0:
        return x
    else:
        return mandelbrot_generator(x, y - 1) ** 2 + x

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """Returns the escape time of a mandelbrot sequence with initial term c

    Parameters:
        c [complex]: the initial term
        max_iterations [int]: the maximum number of iterations

    Returns:
        int: the number of iterations within max_iterations for |z_n| > 2
        None: if |z_n| <= 2 for n = max_iterations

    """
    if abs(mandelbrot_generator(c,max_iterations)) <= 2:
        return None
    else:
        for i in range(max_iterations + 1):
            if abs(mandelbrot_generator(c,i)) > 2:
                return i


