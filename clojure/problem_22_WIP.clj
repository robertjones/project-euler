(require '[clojure.string :as str])

(defn ltrscr [ltr] (.indexOf " ABCDEFGHIJKLMNOPQRSTUVWXYZ" ltr))

(defn wrdscr [wrd] (reduce + (map ltrscr (str/split wrd #""))))

(defn text->lst [text]
  (map
    #(str/replace % #"\"" "") ;; ")
    (str/split text #",")))

(println
  (reduce
    +
    (map-indexed
      #(* (inc %1) (wrdscr %2))
      (sort (text->lst (slurp "p022_names.txt"))))))
