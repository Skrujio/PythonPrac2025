def MINF(f0, f1, *args):
    return lambda x: min([f0(x), f1(x)] + [f(x) for f in args])
