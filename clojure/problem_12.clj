(def tri-nums (reductions + (range)))

(defn sqrt [n]
  (first (filter #(> (* % %) n) (range))))

(defn factors [n]
  (mapcat
    #(if-not (= % (/ n %)) [% (/ n %)] [%])
    (filter #(zero? (mod n %)) (range 1 (sqrt n)))))

(println (first (filter
                  #(> (count (factors %)) 500)
                  tri-nums))) ;; => 76576500
