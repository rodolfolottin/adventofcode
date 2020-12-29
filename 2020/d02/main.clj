(ns main
  (:require [clojure.string :as str]))

(def read-lines
  (->> (slurp "input.txt")
       (str/split-lines)))

(defn regex-find [data] (re-find #"(\d*)-(\d*) (\w): (\w*)" data))

(defn str->int [str] (read-string str))

(defn part-1-valid-password? [data]
  (let [[_ low high chr string] (regex-find data)
        occurrences (count (filter (fn [x] (= chr x)) (str/split string #"")))]
    (and (<= (str->int low) occurrences) (>= (str->int high) occurrences))))

(defn chr-on-sequence-index? [chr index sequence]
  (= chr (nth sequence (- (str->int index) 1))))

(defn xor [a b]
  (cond
    (and (true? a) (true? b)) false
    (true? b) true
    (true? a) true))

(defn part-2-valid-password? [data]
  (let [[_ low high chr string] (regex-find data)
    string-seq (str/split string #"")]
    (xor
     (chr-on-sequence-index? chr low string-seq)
     (chr-on-sequence-index? chr high string-seq))))

(defn solve [valid-password-func]
  (->> read-lines
       (filter valid-password-func)
       (count)))

(println "Part 1 solution" (solve part-1-valid-password?))
(println "Part 2 solution" (solve part-2-valid-password?))
