(defn mult-x? [n x] (= 0 (mod n x)))
(println (reduce + (filter #(or (mult-x? % 3) (mult-x? % 5)) (range 1 1000))))
