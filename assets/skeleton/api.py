class Api:

    __vd = object()
    __fd = object()

    def __init__(self, fd, vd):
        self.__vd = vd
        self.__fd = fd

        self.__vd.set("SKELETON_PREAMBLE", "")
