(defn pad [row] (concat '(0) row '(0)))

(defn diag-step
  [row instruction]
  (map
    (partial apply +)
    (partition 2 1 (instruction row))))

(defn diag-instructions [width]
  (let [grow pad shrink identity]
    (concat (repeat width grow) (repeat width shrink))))

(print (first (reduce diag-step [1] (diag-instructions 20))))
