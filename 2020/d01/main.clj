(ns main
  (:require [clojure.java.io :as io]))

(defn str->int [str] (read-string str))

(def read-lines
  (with-open [rdr (io/reader "input.txt")]
    (map str->int (doall (line-seq rdr)))))

(defn entries-sum-matches-2020? [entry1 entry2]
  (= (+ entry1 entry2) 2020))

(defn main
  [list1 list2]
  (for [col1 list1 col2 list2]
    (if (entries-sum-matches-2020? col1 col2) (* col1 col2))))

(println (filter some? (main read-lines read-lines)))
