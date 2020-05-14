require "./notebook.cr"
require "random"

ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

iterations = 112

results = Array(String).new

def headstails(ran)
    ran >= 0.5_f64
end

for i in (0..iterations).to_a do
    p_1 = headstails(rand) ? "A" : "A"
    p_2 = headstails(rand) ? "A" : "a"
    n_1 = headstails(rand) ? "m" : "m"
    n_2 = headstails(rand) ? "M" : "m"
    results << "#{p_1}#{p_2}#{n_1}#{n_2}"
end

sorted_results = Array(String).new

probabilities = {} of String => Int32

for res in results do 
    sorted = res.chars.sort { |a,b| ALPHABET.index(a.to_s).not_nil! <=> ALPHABET.index(b.to_s).not_nil! }
    sorted_results << sorted.join
end

for r in sorted_results do
    if probabilities.has_key? r
        probabilities[r] += 1
    else
        probabilities[r] = 1
    end
end

for prob in probabilities.keys.to_a do
    puts "#{prob} => #{probabilities[prob]}"
end