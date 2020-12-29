(ns main
  (:require [clojure.string :as str]))

(def read-lines
  (->> (slurp "input.txt")
       (str/split-lines)))

(defn str->int [str] (read-string str))

(defn valid-password? [data]
  (let [[_ low high chr string] (re-find #"(\d*)-(\d*) (\w): (\w*)" data)
        occurrences (count (filter (fn [x] (= chr x)) (str/split string #"")))]
    (and (<= (str->int low) occurrences) (>= (str->int high) occurrences))))

(def part-1
  (->> read-lines
       (filter valid-password?)
       (count)))

(println "Part 1 solution" part-1)
