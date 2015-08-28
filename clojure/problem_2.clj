(def fib (map first (iterate (fn [[a b]] [b (+ a b)]) [1 2])))
(def result (reduce + (filter even? (take-while #(< % 4000000) fib))))
(println result)
