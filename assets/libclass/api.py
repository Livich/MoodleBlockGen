from utilities import StrFormat


class Api:

    __vd = object()
    __fd = object()

    def __init__(self, fd, vd):
        self.__vd = vd
        self.__fd = fd

        sn = vd.get("BLOCKNAME_SHORT")
        vd.set("BLOCKNAME_SHORT_CAM", StrFormat.camel_case(sn))
        inclusion = "require_once($CFG->dirroot.\"/blocks/%s/lib/Blk%s.php\");\n" % (sn, StrFormat.camel_case(sn))
        self.__vd.append("SKELETON_PREAMBLE", "%s" % inclusion)
