#_(defdeps
    [[org.clojure/clojure "1.7.0"]
     [org.clojure/math.numeric-tower "0.0.4"]])

(require '[clojure.math.numeric-tower :as math])

(println (reduce math/lcm (range 1 21)))
