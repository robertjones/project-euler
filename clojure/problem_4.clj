(require '[clojure.string :as s])

(defn palindromic? [number]
  (let [word (str number)]
    (= word (s/reverse word))))

(def palindromics
  (for [x (range 999 99 -1) y (range x 99 -1)
        :let [prod (* x y)]
        :when (palindromic? prod)]
   prod))

(println (apply max palindromics))
