(ns main)

(def read-lines
  (->> (slurp "input.txt")
  (clojure.string/split-lines)
  (map clojure.edn/read-string)))

(defn entries-sum-matches-2020? [entry1 entry2]
  (= (+ entry1 entry2) 2020))

(defn main
  [data]
  (for [col1 data col2 data
        :when (entries-sum-matches-2020? col1 col2)]
     (* col1 col2)))

(println (main read-lines))
