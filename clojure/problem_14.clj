(defn collatz-step [n]
  (if (even? n)
    (/ n 2)
    (+ 1 (* 3 n))))

(defn collatz [start]
  (take-while #(not= % 1) (iterate collatz-step start)))

(defn collatz-len [start] (count (collatz start)))

(def result
  (second
   (apply max-key first
          (map
           #(identity [(collatz-len %) %])
           (range 2 1000000)))))

(println result)
