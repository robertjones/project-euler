(println
 (for [c (range 1 1000) b (range 1 c) a (range 1 b)
       :when (and
              (= 1000 (+ a b c))
              (= (* c c) (+ (* a a) (* b b))))]
   (* a b c)))