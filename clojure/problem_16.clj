#_(defdeps
    [[org.clojure/clojure "1.7.0"]
     [org.clojure/math.numeric-tower "0.0.4"]])

(require '[clojure.math.numeric-tower :as math])
(require '[clojure.string :as string])

(defn num->digs [x] (map read-string (string/split (str x) #"")))

(println (apply + (num->digs (math/expt 2 1000))))
