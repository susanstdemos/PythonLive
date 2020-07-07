from buildbot.status.web import waterfall
from mercurial import subrepo
import test


def main():
    x = 3
    print(x)

    ##vulnerable function called
    vln = waterfall.WaterfallStatusResource()
    vln.body(None)

    ######vulneable function
    ## subrepo() --> _auditsubrepopath() [vulnerable]
    subrepo.subrepo(None, None)


if '__main__' == __name__:
    main()
    test.filter()
