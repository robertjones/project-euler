(defn sum-sq [nums] (reduce + (map #(* % %) nums)))

(defn sq-sum [nums] (#(* % %) (reduce + nums)))

(println (- (sq-sum (range 101)) (sum-sq (range 101))))
