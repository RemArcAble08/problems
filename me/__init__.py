import check50
import check50.c
import re


@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")


@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)


@check50.check(compiles)
def emma():
    """responds to name Mario"""
    check_name("Mario")


@check50.check(compiles)
def inno():
    """responds to name Peach"""
    check_name("Peach")


@check50.check(compiles)
def kamryn():
    """responds to name Bowser"""
    check_name("Bowser")


def check_name(name):
    output = check50.run("./hello").stdin(name).stdout()
    if not re.match(regex(name), output):
        if output[-1] != "\n":
            raise check50.Mismatch(
                f"hello, {name}\n",
                actual=output,
                help=r"Did you forget a \n at the end of your output?",
            )
        raise check50.Mismatch(f"hello, {name}\n", actual=output)


def regex(string):
    return f"^[Hh]ello, {re.escape(string)}\n$"
