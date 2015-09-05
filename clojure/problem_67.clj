;; Text processing

(defn parse-int [x] (int (bigint x)))

(defn text->grid [text]
  (map
    #(map parse-int (clojure.string/split % #" "))
    (clojure.string/split text #"\n")))

;; Max path sum finding

(defn path-step [acc step]
  (map
    +
    step
    (map (partial apply max) (partition 2 1 acc))))

(defn max-path [grid]
  (apply max (reduce path-step (reverse grid))))

;; Solve

(println (max-path (text->grid (slurp "p067_triangle.txt"))))
