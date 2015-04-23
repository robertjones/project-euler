from collections import namedtuple


def dig_top_bottom(numer, denom):
    return (int(num) for num in set(str(numer)) if num in str(denom))


def cancel(num, cancelled):
    return int(str(num).replace(str(cancelled), '', 1))


def is_cancelling(numer, denom, cancld):
    try:
        return numer / denom == cancel(numer, cancld) / cancel(denom, cancld)
    except ZeroDivisionError:
        return False

CanFrac = namedtuple('CanFrac', ['numer', 'denom', 'can'])

cancelling = [CanFrac(numer, denom, cancelled)
              for denom in range(10, 100)
              for numer in range(10, denom)
              for cancelled in dig_top_bottom(numer, denom)
              if cancelled != 0
              if is_cancelling(numer, denom, cancelled)
              ]

cancelled_fracs = [(cancel(frac.numer, frac.can), cancel(frac.denom, frac.can))
                   for frac in cancelling]

print(cancelled_fracs)
