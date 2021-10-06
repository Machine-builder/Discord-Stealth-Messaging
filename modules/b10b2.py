class b10b2():
    @staticmethod
    def base10base2( base10string ):
        return bin(base10string)[2:]
    @staticmethod
    def base2base10( base2string ):
        return int(base2string, 2)