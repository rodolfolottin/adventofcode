(ns main)

(def read-lines
  (->> (slurp "input.txt")
  (clojure.string/split-lines)
  (map clojure.edn/read-string)))

(defn entries-sum-matches-2020? [entries]
  (= (reduce + entries) 2020))

(defn main
  [data]
  (for [col1 data col2 data
        :let [values [col1 col2]]
        :when (entries-sum-matches-2020? values)]
     (reduce * values)))

(defn main-part-two
  [data]
  (for [col1 data col2 data col3 data
        :let [values [col1 col2 col3]]
        :when (entries-sum-matches-2020? values)]
     (reduce * values)))


(println "Part 1 solution" (first (main read-lines)))
(println "Part 2 solution" (first (main-part-two read-lines)))
