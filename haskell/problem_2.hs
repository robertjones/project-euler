fibs = 1 : 2 : zipWith (+) fibs (tail fibs)
main = print $ sum [ x | x <- takeWhile (< 4*10^6) fibs, even x]
