
__all__ = [
        "convert_base"
    ]

"""
convert_base(str(abs(num)),
             int(to_base)=10,
             int(from_base)=10
             ) => str(answer)
bases: [2-36]
"""

def convert_base(num:str, to_base:int=10, from_base:int=10):
    """
convert_base(str(abs(num)),
             int(to_base)=10,
             int(from_base)=10
             ) => str(answer)
bases: [2-36]
"""
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]



    
